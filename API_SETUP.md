# 🔑 API Key Setup Guide

The Student Performance Analysis app uses Groq AI to provide intelligent, personalized insights. You need a free API key to enable the AI features.

## 🚀 Quick Setup

### Option 1: Use the Setup Script (Recommended)
```bash
python3 setup_api_key.py
```

### Option 2: Manual Setup

1. **Get a free Groq API key:**
   - Go to: https://console.groq.com/
   - Sign up or log in
   - Navigate to "API Keys" section
   - Create a new API key
   - Copy the key

2. **Configure the key:**
   - Open `config.py` in a text editor
   - Replace `your_groq_api_key_here` with your actual API key
   - Save the file

3. **Alternative: Environment Variable**
   ```bash
   export GROQ_API_KEY="your_actual_api_key_here"
   python3 app.py
   ```

## ✅ Verify Setup

Run the app and check the console output:
```bash
python3 app.py
```

You should see:
- ✅ `Groq AI client initialized successfully`

If you see warnings about missing API key, follow the setup steps above.

## 🛠️ Troubleshooting

### "AI service is not configured" error
- **Cause**: API key not set or invalid
- **Solution**: Follow the setup steps above

### "AI service is currently unavailable" error
- **Cause**: Network issues or API problems
- **Solution**: Check your internet connection and try again

### API key not working
- **Cause**: Invalid or expired key
- **Solution**: Generate a new key from https://console.groq.com/

## 🔒 Security Notes

- Keep your API key private and secure
- Don't commit API keys to version control
- Use environment variables in production
- The free Groq tier is sufficient for this application

## 💡 About Groq

Groq provides fast, efficient AI inference with generous free usage limits. Perfect for educational applications like this student performance analyzer.

---

**Need help?** Check the console output when running the app - it provides detailed error messages and setup instructions.