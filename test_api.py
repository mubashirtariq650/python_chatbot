import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure DeepSeek via OpenRouter API
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

try:
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[{"role": "user", "content": "Say hello in a friendly way"}],
        max_tokens=50
    )
    print('✅ OpenAI API is working!')
    print('Response:', response.choices[0].message.content)
except Exception as e:
    error_str = str(e)
    if "401" in error_str:
        print('❌ API Key Error: Invalid DeepSeek/OpenRouter API key')
        print('   Get your key from: https://openrouter.ai/')
    elif "429" in error_str:
        print('⚠️  Rate Limited: Too many requests')
    elif "insufficient_quota" in error_str.lower():
        print('⚠️  Quota Exceeded: Check your account at https://openrouter.ai/')
    else:
        print('❌ DeepSeek API error:', error_str)
    print('Make sure your DEEPSEEK_API_KEY is set correctly in the .env file')