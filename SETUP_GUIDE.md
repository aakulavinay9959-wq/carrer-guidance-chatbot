"""
Career Guidance Chatbot - Setup & Configuration Guide
"""

# SETUP INSTRUCTIONS

## 1. GEMINI API (For Chatbot Responses)

### Get API Key:
1. Go to https://aistudio.google.com
2. Click on "Get API Key"
3. Create a new API key
4. Copy the key

### Set Environment Variable:

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your_api_key_here
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY="your_api_key_here"
```

**Permanent Setup (Windows):**
1. Press `Win + X` → System Settings
2. Advanced → Environment Variables
3. New User Variable:
   - Variable name: GEMINI_API_KEY
   - Variable value: your_api_key_here
4. Restart terminal/IDE


## 2. NEWS API (For Live News)

### Get API Key:
1. Go to https://newsapi.org
2. Click on "Get API Key"
3. Sign up for free tier (100 requests per day)
4. Copy your API key

### Set Environment Variable:

**Windows (PowerShell):**
```powershell
$env:NEWS_API_KEY="your_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set NEWS_API_KEY=your_api_key_here
```

**Linux/Mac:**
```bash
export NEWS_API_KEY="your_api_key_here"
```

**Permanent Setup (Windows):**
1. Press `Win + X` → System Settings
2. Advanced → Environment Variables
3. New User Variable:
   - Variable name: NEWS_API_KEY
   - Variable value: your_api_key_here
4. Restart terminal/IDE


## 3. Running the Application

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Start the App:
```bash
streamlit run demo2.py
```

The app will open at: http://localhost:8501


## 4. Features

### Home Page:
- Career Guidance Chatbot
- AI-powered responses
- Career path recommendations
- Roadmap options

### News Page:
- Live news from internet
- Search and filter
- Latest career-related articles
- Newsletter subscription

### Profile Page:
- User authentication
- Login/Signup
- Profile management
- Settings


## 5. File Structure

```
nextstep/
├── demo2.py              # Main entry point
├── config.py             # Configuration & constants
├── styles.py             # Styling functions
├── chatbot.py            # Gemini API integration
├── ui.py                 # Main UI components
├── navbar.py             # Navigation bar
├── news.py               # News fetching & display
├── profile.py            # User profile & auth
└── requirements.txt      # Python dependencies
```


## 6. Environment Variables Summary

| Variable | Source | Purpose |
|----------|--------|---------|
| GEMINI_API_KEY | https://aistudio.google.com | AI chatbot responses |
| NEWS_API_KEY | https://newsapi.org | Live news fetching |

## 7. Troubleshooting

### "API Key Not Found" Error:
- Check if environment variable is set correctly
- Restart terminal/IDE after setting variable
- Test with: `echo %GEMINI_API_KEY%` (Windows) or `echo $GEMINI_API_KEY` (Linux)

### News Not Loading:
- Ensure NEWS_API_KEY is set
- Check internet connection
- Free tier: 100 requests/day limit
- Fallback news shows if API is unavailable

### ImportError:
- Run: `pip install -r requirements.txt`
- Or individual: `pip install streamlit google-genai requests`

### Port Already in Use:
- Use different port: `streamlit run demo2.py --server.port 8502`


## 8. Free Tier Limits

**Gemini API:**
- Free tier available
- Rate limits apply
- Check: https://ai.google.dev/pricing

**News API:**
- 100 requests/day (free tier)
- Good for testing (≈10 news articles = 1 request)
- Paid plans available


## 9. License & Credits

- **Streamlit**: https://streamlit.io
- **Google Generative AI**: https://ai.google.dev
- **NewsAPI**: https://newsapi.org


## 10. Support

For issues or questions:
1. Check the setup guide above
2. Review error messages carefully
3. Ensure all API keys are valid
4. Check API rate limits
