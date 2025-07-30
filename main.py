import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    verbose = False
    model = "gemini-2.0-flash-001"
    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

    _ = load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        sys.exit(1)
    user_prompt = sys.argv[1]

    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        verbose = True
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    resp = client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )
    print(resp.text)
    if verbose and resp.usage_metadata:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {resp.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
