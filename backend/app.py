from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Supported languages with their codes
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'kn': 'Kannada',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'gu': 'Gujarati',
    'bn': 'Bengali',
    'pa': 'Punjabi',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ja': 'Japanese',
    'zh': 'Chinese',
    'ko': 'Korean'
}

@app.route('/')
def index():
    """Serve the index.html template"""
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    """Translate text between languages"""
    try:
        data = request.json
        text = data.get('text', '')
        source_lang = data.get('source_lang', 'en')
        target_lang = data.get('target_lang', 'kn')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Validate language codes
        if source_lang not in SUPPORTED_LANGUAGES or target_lang not in SUPPORTED_LANGUAGES:
            return jsonify({'error': 'Unsupported language'}), 400
        
        # Use MyMemory Translation API (free, no API key required)
        translated_text = translate_via_mymemory(text, source_lang, target_lang)
        
        return jsonify({
            'success': True,
            'original': text,
            'translated': translated_text,
            'source_language': SUPPORTED_LANGUAGES[source_lang],
            'target_language': SUPPORTED_LANGUAGES[target_lang]
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def translate_via_mymemory(text, source_lang, target_lang):
    """Translation using MyMemory API (free)"""
    try:
        url = "https://api.mymemory.translated.net/get"
        langpair = f"{source_lang}|{target_lang}"
        params = {
            'q': text,
            'langpair': langpair
        }
        response = requests.get(url, params=params, timeout=10)
        result = response.json()
        
        if result['responseStatus'] == 200:
            return result['responseData']['translatedText']
        else:
            return text  # Return original if translation fails
    except Exception as e:
        print(f"Translation error: {e}")
        return text

@app.route('/languages', methods=['GET'])
def get_languages():
    """Get list of supported languages"""
    return jsonify({
        'languages': SUPPORTED_LANGUAGES
    })

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)