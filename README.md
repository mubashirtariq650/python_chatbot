# OpenAI Chatbot

A simple Python chatbot powered by OpenAI's GPT models.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get your OpenAI API key:**
   - Go to [OpenAI Platform](https://platform.openai.com/)
   - Sign up or log in
   - Navigate to API Keys section
   - Create a new API key

3. **Configure your API key:**
   - Open the `.env` file
   - Replace `your_api_key_here` with your actual OpenAI API key

## Usage

Run the chatbot:
```bash
python main.py
```

Start chatting! Type your messages and the bot will respond. Type 'quit', 'exit', or 'bye' to end the conversation.

## Features

- Conversational AI using OpenAI's GPT models
- Maintains conversation history
- Simple command-line interface
- Error handling for API issues

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection

## Customization

You can modify the chatbot behavior by:
- Changing the model (e.g., to `gpt-4` if you have access)
- Adjusting `max_tokens` for longer/shorter responses
- Modifying the `temperature` for more/less creative responses
- Updating the system message in the `messages` list