import os
from flask import Flask, render_template, request, jsonify, session
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = "supersecretkey"  # session ke liye

# Configure DeepSeek via OpenRouter API
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

@app.route("/")
def home():
    return render_template("index.html")

# Send chat message
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=messages,
            max_tokens=300,
            temperature=0.7
        )
        bot_reply = response.choices[0].message.content
        return jsonify({"reply": bot_reply})

    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg or "invalid" in error_msg.lower():
            error_msg = "API key is invalid. Please check your DEEPSEEK_API_KEY in the .env file."
        elif "429" in error_msg:
            error_msg = "Too many requests. Please try again later."
        elif "insufficient_quota" in error_msg.lower():
            error_msg = "OpenRouter quota exceeded. Please check your account at https://openrouter.ai/"
        else:
            error_msg = "Server error. Please try again later."
        return jsonify({"error": error_msg}), 500

if __name__ == "__main__":
    app.run(debug=True)