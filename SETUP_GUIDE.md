# Quick Setup & Running Guide

## Prerequisites
- Python 3.7+
- Modern web browser (Chrome, Firefox, Edge, Safari)
- Microphone (for voice features)

## Installation

### 1. Install Backend Dependencies

Navigate to the backend folder and install requirements:

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the Backend Server

```bash
python app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

### 3. Open the Frontend

Open the `frontend/index.html` file in your web browser, or:

```bash
# Option 1: Direct file
Open frontend/index.html in your browser

# Option 2: Simple Python HTTP Server
cd frontend
python -m http.server 8000
# Then open http://localhost:8000 in your browser
```

## Using the Three Modes

### Mode 1: Text to Text
1. Select "Text to Text" button
2. Choose source and target languages from dropdowns
3. Type or paste text in the left panel
4. Click "Translate" button
5. See translation in the right panel

### Mode 2: Voice to Text
1. Select "Voice to Text" button
2. Choose your source language
3. Click "Start Recording"
4. Speak clearly into your microphone
5. Click "Stop Recording"
6. Your speech is transcribed to text

### Mode 3: Voice to Voice
1. Select "Voice to Voice" button
2. Choose source and target languages
3. Click "Start Recording"
4. Speak your message
5. Click "Stop Recording"
6. System automatically:
   - Converts speech to text
   - Translates text
   - Speaks the translation

## Available Actions

| Button | Purpose | Shortcut |
|--------|---------|----------|
| Translate | Convert text | Ctrl+Enter |
| Speak | Hear pronunciation | N/A |
| Start Recording | Begin voice input | N/A |
| Copy | Copy translation to clipboard | N/A |
| Download | Save translation as file | N/A |
| Clear | Clear all text fields | N/A |
| Swap | Switch source & target languages | N/A |

## Supported Language Pairs

### Indian Languages
- English ↔ Hindi
- English ↔ Kannada
- English ↔ Tamil
- English ↔ Telugu
- English ↔ Malayalam
- English ↔ Marathi
- English ↔ Gujarati
- English ↔ Bengali
- English ↔ Punjabi
- And many more combinations...

### International Languages
- English ↔ Spanish
- English ↔ French
- English ↔ German
- English ↔ Italian
- English ↔ Portuguese
- English ↔ Russian
- English ↔ Japanese
- English ↔ Chinese
- English ↔ Korean

## Troubleshooting

### Microphone Issues
- **Check browser permissions**: Allow microphone access
- **Try different browser**: Some browsers have better speech recognition
- **Check microphone**: Ensure your microphone is working in system settings

### Backend Connection Error
- Ensure `python app.py` is running
- Check that port 5000 is not in use
- Verify backend is running on `http://127.0.0.1:5000`

### Translation Not Working
- Check internet connection (uses online API)
- Try different language combination
- Verify both language codes are valid

### Voice Not Recognized
- Speak clearly and slowly
- Ensure correct language is selected
- Check microphone volume level

## Features Overview

✅ **Text Translation** - Translate between 20+ languages  
✅ **Voice to Text** - Convert speech to text  
✅ **Voice to Voice** - Complete voice translation  
✅ **Text-to-Speech** - Hear pronunciation  
✅ **Download** - Save translations locally  
✅ **Copy** - One-click clipboard copy  
✅ **Language Swap** - Quickly reverse languages  
✅ **Real-time Character Count** - Track text length  
✅ **Responsive Design** - Works on all devices  
✅ **Modern UI** - Beautiful gradient interface  

## Project Structure

```
Translator/
├── backend/
│   ├── app.py              # Flask server
│   └── requirements.txt    # Python dependencies
├── frontend/
│   └── index.html          # Main web interface
├── README.md               # Original documentation
├── FEATURES.md             # New features guide
├── requirements.txt        # Project dependencies
└── run.bat / START.bat     # Windows batch files
```

## API Endpoints

### `/translate` (POST)
Translates text between languages

**Request:**
```json
{
  "text": "Hello, how are you?",
  "source_lang": "en",
  "target_lang": "kn"
}
```

**Response:**
```json
{
  "success": true,
  "original": "Hello, how are you?",
  "translated": "ನಮಸ್ಕಾರ, ನೀವು ಹೇಗಿದ್ದೀರಿ?",
  "source_language": "English",
  "target_language": "Kannada"
}
```

### `/languages` (GET)
Gets list of supported languages

**Response:**
```json
{
  "languages": {
    "en": "English",
    "kn": "Kannada",
    "hi": "Hindi",
    ...
  }
}
```

### `/health` (GET)
Checks if server is running

**Response:**
```json
{
  "status": "healthy"
}
```

## Tips for Best Results

1. **Speak Clearly**: Enunciate words properly for voice recognition
2. **Natural Language**: Use complete sentences for better translations
3. **One Language at a Time**: Don't mix languages in voice input
4. **Adjust Microphone**: Position microphone 6-12 inches from mouth
5. **Quiet Environment**: Minimize background noise for voice recognition

## Performance Notes

- Translations use free online API (MyMemory)
- First translation may take 1-2 seconds
- Voice recognition depends on browser and microphone
- No data is stored on server (stateless)
- No personal data collection

---

**Happy Translating!** 🌍🗣️
