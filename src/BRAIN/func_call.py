from typing import Union 
from src.BRAIN.lm_ai import client
import json 
import re

TOOLS = "src/DATA/tools.json"

def load_tools(file_path: str) -> Union[dict, list]:
    try:
        with open(file_path, "r") as file:
            tools = json.load(file)
            return tools
    except FileNotFoundError:
        print("Error: Tools configuration file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []

def load_tools_message(file_path: str) -> str:
    tools = load_tools(file_path)
    return json.dumps(tools, indent=2)

# Define system message for guiding the AI
SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a function-calling AI model. You are provided with function signatures "
        f"within <tools> {load_tools_message(TOOLS)} </tools> XML tags. "
        "For each user query, extract the most relevant parameters from the input and select the most appropriate function. "
        "Return the exact tool call in this format:\n\n"
        "<tool_call>\n"
        '{"name": "<function-name>", "arguments": <args-dict>}\n'
        "</tool_call>\n\n"
        "Ensure that extracted parameters match the function signature exactly. "
        "Return only the function call in the specified format without explanations or extra content."
    ),
}


def parse_tool_call(response: str) -> Union[dict, None]:
    match = re.search(r"<tool_call>\s*(\{.*?\})\s*</tool_call>", response, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1).replace("'", '"'))
        except json.JSONDecodeError as e:
            print(f"Error parsing function call JSON: {e}")
    else:
        print("No function call data found.")
    return None

def create_function_call(user_query: str) -> Union[str, None]:
    messages = [SYSTEM_MESSAGE, {"role": "user", "content": user_query}]

    try:
        completion = client.chat.completions.create(
            model="NousResearch/Hermes-2-Pro-Mistral-7B-GGUF",
            # model="heBloke/Mistral-7B-Instruct-v0.2-GGUF",
            messages=messages,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error creating function call: {e}")
    return None 


if __name__ == "__main__":
    ...
    