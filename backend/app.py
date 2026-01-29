from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate_text():
    """Translate English text to Kannada"""
    try:
        data = request.json
        english_text = data.get('text', '')
        
        if not english_text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Use MyMemory Translation API (free, no API key required)
        kannada_text = translate_via_mymemory(english_text)
        
        return jsonify({
            'success': True,
            'english': english_text,
            'kannada': kannada_text
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def translate_via_mymemory(text):
    """Translation using MyMemory API (free)"""
    try:
        url = "https://api.mymemory.translated.net/get"
        params = {
            'q': text,
            'langpair': 'en|kn'
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

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
