#!/usr/bin/env python3
"""
Helper script to set up your Groq API key for the Student Performance Analysis app.
"""

import os
import sys

def setup_groq_api_key():
    print("🎓 Student Performance Analysis - API Key Setup")
    print("=" * 50)
    print()
    
    print("This app uses Groq AI for intelligent analysis.")
    print("You need a free API key from Groq to use the AI features.")
    print()
    
    # Check if key is already set
    try:
        from config import GROQ_API_KEY
        if GROQ_API_KEY != "your_groq_api_key_here" and GROQ_API_KEY:
            print("✅ API key is already configured!")
            print(f"   Current key: {GROQ_API_KEY[:20]}...")
            response = input("\nDo you want to update it? (y/N): ").strip().lower()
            if response != 'y':
                print("Setup cancelled.")
                return
    except ImportError:
        pass
    
    print("📋 Steps to get your free Groq API key:")
    print("1. Go to: https://console.groq.com/")
    print("2. Sign up or log in")
    print("3. Navigate to API Keys section")
    print("4. Create a new API key")
    print("5. Copy the key and paste it below")
    print()
    
    while True:
        api_key = input("Enter your Groq API key: ").strip()
        
        if not api_key:
            print("❌ Please enter a valid API key.")
            continue
            
        if len(api_key) < 20:
            print("❌ API key seems too short. Please check and try again.")
            continue
            
        # Confirm the key
        print(f"\n📝 You entered: {api_key[:20]}...")
        confirm = input("Is this correct? (y/N): ").strip().lower()
        
        if confirm == 'y':
            break
        else:
            print("Let's try again...")
    
    # Update config.py
    try:
        # Read current config
        config_content = f'''import os

# Groq API Key - Set this to your actual API key
# You can also set it as an environment variable: export GROQ_API_KEY="your_key_here"
GROQ_API_KEY = "{api_key}"

# If no API key is set, provide a helpful message
if GROQ_API_KEY == "your_groq_api_key_here":
    print("Warning: GROQ_API_KEY not set! Please set your Groq API key in config.py or as an environment variable.")
    print("You can get a free API key from: https://console.groq.com/")
'''
        
        with open('config.py', 'w') as f:
            f.write(config_content)
        
        print("\n✅ API key saved successfully!")
        print("🚀 You can now run the app with: python3 app.py")
        print("\nThe AI features should now work properly!")
        
    except Exception as e:
        print(f"\n❌ Error saving API key: {e}")
        print("You can manually edit config.py and replace 'your_groq_api_key_here' with your API key.")

if __name__ == "__main__":
    setup_groq_api_key()