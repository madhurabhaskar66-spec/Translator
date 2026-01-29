# English to Kannada Translator with Text-to-Speech

A fullstack translator application that converts English text to Kannada with integrated text-to-speech functionality.

## Features

- 🌐 **English to Kannada Translation** - Real-time translation using MyMemory API
- 🔊 **Text-to-Speech** - Listen to both English and Kannada pronunciations
- 📋 **Copy to Clipboard** - Easy sharing of translations
- 🎨 **Modern UI** - Clean, responsive interface
- ⌨️ **Keyboard Shortcuts** - Use Ctrl+Enter to translate
- 📱 **Mobile Responsive** - Works on desktop and mobile devices

## Project Structure

```
Translator/
├── backend/
│   ├── app.py                 # Flask backend application
│   └── requirements.txt       # Python dependencies
├── frontend/
│   └── index.html            # Frontend HTML with CSS and JavaScript
└── README.md                 # This file
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser with Web Speech API support

## Installation

### 1. Install Python Dependencies

Navigate to the backend folder and install required packages:

```bash
cd backend
pip install -r requirements.txt
```

**Dependencies:**
- Flask - Web framework
- flask-cors - CORS support for cross-origin requests
- requests - HTTP library for API calls
- python-dotenv - Environment variable management
- google-cloud-translate - Optional Google Cloud translation

## Running the Application

### Step 1: Start the Backend Server

```bash
cd backend
python app.py
```

The backend will start on `http://localhost:5000`

You should see output like:
```
 * Running on http://127.0.0.1:5000
```

### Step 2: Open the Frontend

1. Navigate to the `frontend` folder
2. Open `index.html` in your web browser
   - Simply double-click the file, or
   - Use a local server:
     ```bash
     # Using Python 3
     python -m http.server 8000
     
     # Then open http://localhost:8000 in your browser
     ```

## Usage

1. **Enter English Text**: Type or paste English text in the left text area
2. **Translate**: Click the "Translate" button (or press Ctrl+Enter)
3. **Listen**: 
   - Click "🔊 Speak" button to hear the English pronunciation
   - Click "🔊 Speak" in the Kannada section to hear Kannada pronunciation
4. **Copy**: Click "📋 Copy" to copy the translation to clipboard
5. **Clear**: Click "🗑️ Clear" to reset both text areas

## API Endpoints

### POST `/translate`

Translates English text to Kannada.

**Request:**
```json
{
  "text": "Hello World"
}
```

**Response:**
```json
{
  "success": true,
  "english": "Hello World",
  "kannada": "ಹಲೋ ವರ್ಲ್ಡ"
}
```

### GET `/health`

Health check endpoint to verify backend is running.

**Response:**
```json
{
  "status": "healthy"
}
```

## Translation Services

The application uses **MyMemory Translation API** (free, no API key required) for translation. 

### Optional: Using Google Cloud Translation

For better translations, you can set up Google Cloud Translation:

1. Create a Google Cloud project and enable the Translation API
2. Create a service account and download the JSON key
3. Set the environment variable:
   ```bash
   set GOOGLE_APPLICATION_CREDENTIALS=path/to/your/key.json
   ```
4. The app will automatically use Google Cloud API if credentials are available

## Browser Compatibility

- **Chrome/Chromium**: Full support for Web Speech API
- **Firefox**: Full support for Web Speech API
- **Safari**: Full support for Web Speech API
- **Edge**: Full support for Web Speech API

## Troubleshooting

### Backend not connecting
- Ensure the backend is running on `http://localhost:5000`
- Check that port 5000 is not in use
- Look for error messages in the terminal

### Translation not working
- Check your internet connection
- The MyMemory API requires internet access
- Try with shorter text first

### Text-to-Speech not working
- Ensure your browser supports Web Speech API
- Check browser permissions for audio
- Try a different language setting
- Some Kannada voices might not be available on all systems

### CORS errors
- The backend has CORS enabled, should not be an issue
- If problems persist, check Flask-CORS is installed

## Development

To modify the translation service:

1. Edit `backend/app.py` to add/change translation providers
2. Modify `frontend/index.html` for UI changes
3. Restart the backend for code changes to take effect
4. Refresh the browser to see frontend changes

## Future Enhancements

- [ ] Add voice input (speech-to-text for Kannada)
- [ ] Support more language pairs
- [ ] Add translation history
- [ ] Improve translation quality with advanced APIs
- [ ] Add offline translation support
- [ ] User authentication for saving favorites
- [ ] Database for storing translations
- [ ] Mobile app wrapper

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please check:
1. Backend logs in the terminal
2. Browser console (F12 → Console tab)
3. Ensure all dependencies are installed

Enjoy translating! 🌐✨
