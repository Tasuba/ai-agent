import os
import sys
from call_function import available_functions
from prompts import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import Client, types


MODEL = "gemini-2.0-flash-001"


def main():
    _ = load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client, messages, verbose)



def generate_content(client: Client, messages: list[types.Content], verbose: bool) -> None:
    resp = client.models.generate_content(
        model=MODEL,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        ),
    )

    if verbose and resp.usage_metadata:
        print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {resp.usage_metadata.candidates_token_count}")

    if not resp.function_calls:
        print(resp.text)
        return

    for function_call_part in resp.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")


if __name__ == "__main__":
    main()