from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
from translate import Translator
import logging

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
        
        # Skip translation if source and target are the same
        if source_lang == target_lang:
            return jsonify({
                'success': True,
                'original': text,
                'translated': text,
                'source_language': SUPPORTED_LANGUAGES[source_lang],
                'target_language': SUPPORTED_LANGUAGES[target_lang]
            })
        
        # Use translation with fallback
        translated_text = translate_text_with_fallback(text, source_lang, target_lang)
        
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
    """Translation using MyMemory API (backup only)"""
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
            translated = result['responseData']['translatedText']
            # Check if translation is valid
            if translated and translated.strip() and translated.lower() != text.lower():
                return translated
        return None
    except Exception as e:
        logger.error(f"MyMemory translation error: {e}")
        return None

def translate_via_translate_lib(text, source_lang, target_lang):
    """Translation using translate library (primary method)"""
    try:
        translator = Translator(from_lang=source_lang, to_lang=target_lang)
        translated = translator.translate(text)
        
        if translated and translated.strip():
            return translated
        return None
    except Exception as e:
        logger.error(f"Translate library error: {e}")
        return None

def translate_text_with_fallback(text, source_lang, target_lang):
    """Try translate library first, fall back to MyMemory"""
    # Try translate library (uses Google Translate backend)
    translated = translate_via_translate_lib(text, source_lang, target_lang)
    if translated:
        return translated
    
    # Fall back to MyMemory
    translated = translate_via_mymemory(text, source_lang, target_lang)
    if translated:
        return translated
    
    # If both fail, return original text
    logger.warning(f"Translation failed for: {text} ({source_lang}->{target_lang})")
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