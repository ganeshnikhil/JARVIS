

from openai import OpenAI
import json 
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def send_to_ai(prompt, max_token = 2000 , model="NousResearch/Hermes-2-Pro-Mistral-7B-GGUF") -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an intelligent system designed to serve . Please do the task as requested by the user. Follow the instructions carefully and perform the action."},
                {"role": "user", "content": str(prompt)}
            ],
            temperature=0.8,
            max_tokens=max_token,
            top_p=1
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     text = "Schedule a meeting about project updates on Dec 5th, mark it as High Priority, and add tags 'Work' and 'Urgent'. phone no of client is 9835872530"
#     prompt = r'''
# JSON Template:
# {{
#     "task": {{
#         "title": null,
#         "description": null,
#         "priority": null,
#         "category_id": null,
#         "is_recurring": false,
#         "recurrence_pattern": null,
#         "voice_command_key": null,
#         "Phone_no":null,
#         "tags": [],
#         "time_tracking": {{
#             "due_date": null
#         }}
#     }}
# }}

# Text: {0}

# ### Task:
# Extract the relevant details from the text and populate the JSON fields. Return only the filled JSON, with no explanations or extra text.'''.format(text)
#     response = send_to_ai(prompt)
#     print(response)
#     # If the response includes extra text, we'll attempt to extract the JSON portion only
# try:
#     # Attempt to parse the response and retrieve the JSON content only
#     dict_data = json.loads(response)
#     print(dict_data['task'])
# except json.JSONDecodeError:
#     # If the model included irrelevant text, try to isolate the JSON part (this will depend on your response format)
#     # This assumes the JSON starts with '{' and ends with '}' at the first level
#     start = response.find('{')
#     end = response.rfind('}') + 1
#     if start != -1 and end != -1:
#         json_part = response[start:end]
#         dict_data = json.loads(json_part)
#         print(dict_data['task'])
#     else:
#         print("Error: No valid JSON found in the response.")
