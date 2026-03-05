# CLI Chatbot

A simple general assistant chatbot used in the command-line to answer any questions a user might have

## Quick Start

### Prerequisites
- Python 3.11 or higher
- pip package manager
- Anthropic API key

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd "cli-chatbot"
```
2. Create a virtual environment and activate it
```bash
python -m venv venv
```
- Windows Activation
```bash
venv\Scripts\activate.bat
```
- Mac/Linux Activation
```bash
source venv/bin/activate
```

3. Install dependencies for virtual envrionment
```bash
pip install -r requirements.txt
```

4. Configure API credentials and place in .env file
```
ANTHROPIC_API_KEY="your-api-key-here"
```

### How to use
1. Open virtual environment
2. Run the code using python cli_chatbot.py
3. Type in request to Claude and await response
4. When finished type 'quit'

### Configuration
- Model used: Claude Haiku 4.5 
- Context window: 200k tokens
- Warning threshold before reaching context window is at 85% capacity

## Author

Keyshawn Felton

## Acknowledgments

This project was built using the following tools and technologies:

**Development Tools:**
- Claude (Anthropic) - AI guided development, code review, and debugging support

**Core Technologies:**
- Anthropic API - Powers AI-generated responses

## License

MIT License