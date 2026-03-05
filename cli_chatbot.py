import os
import anthropic
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
message_history = []
system_prompt = "You are a polite, empathetic, and efficient general assistant. Your goal is to help users with what they ask. Try to be as concise as possible and avoid using jargon."
context_window_limit = 200000
context_threshold = 0.85
model = "claude-haiku-4-5"

while (True):
    user_input = input("Please type in your message: ")
    if (user_input == "quit"):
        print("Closing session")
        break
    if (not user_input):
        print("No message sent received")
        continue

    message_history.append({
            "content": user_input,
            "role": "user"
            })
      
    token_count = client.messages.count_tokens(model=model, messages=message_history).input_tokens
    if (token_count > context_window_limit):
        print("This request will surpass the context window limit and will not be performed. Please retry this request or start a new session")
        message_history.pop()
        continue
    elif (token_count > context_window_limit * context_threshold):
        print("Warning, you are nearly at this model's token limit (85 percent capacity)")

    try:
        with client.messages.stream(
            max_tokens=1024,
            messages=message_history,
            model=model,
            system= system_prompt
        ) as stream:
            print("Claude: ", end="")
            response = ''
            for text in stream.text_stream:
                print(text, end='', flush=True)
                response += text
            print()    

        message_history.append({
            "content": response,
            "role": "assistant"
        })
    except anthropic.APIConnectionError as e:
        print("The server could not be reached, please try again later")
        message_history.pop()
    except anthropic.RateLimitError as e:
        print("Too many requests or tokens used, try waiting up to a minute before sending in more requests")
        message_history.pop()
    except anthropic.APIStatusError as e:
        print("Request unsuccessful, please try again later")
        message_history.pop()