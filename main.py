import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("User prompt required")
        sys.exit(1)
    user_prompt = sys.argv[1]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=user_prompt
    )
    if sys.argv[2] == "--verbose":
        print("User prompt: ", user_prompt)
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)
    print(response.text)


if __name__ == "__main__":
    main()
