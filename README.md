
# JARVIS

# Jarvis AI Assistant

Welcome to the Jarvis AI Assistant project! This AI-powered assistant can perform various tasks such as providing weather reports, summarizing news headlines, sending emails, and more, all through voice commands. Below, you will find detailed instructions on how to set up, use, and interact with this application.

## Features

- **Voice Activation**: Say "Hey Jarvis" to activate listening mode.
- **Speech Recognition**: Recognizes and processes user commands via speech input.
- **AI Responses**: Provides responses using AI-generated text-to-speech output.
- **Task Execution**: Handles multiple tasks, including:
  - Sending emails
  - Summarizing weather reports
  - Reading news headlines
  - General AI-based tasks
- **Timeout Handling**: Automatically deactivates listening mode after 5 minutes of inactivity.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.9 or later**
- Required libraries (listed in `requirements.txt`)

### Configuration

1. **Create a `.env` file** in the root directory of the project.

2. **Add your API keys and other configuration variables** to the `.env` file. Here’s a sample structure:

   ```dotenv
   Weather_api=your_weather_api_key
   News_api=your_news_api_key
   Sender_email = your_email
   Receiver_email = subject_email
   Password_email = email_password.
   ```
3. **Setup the keys and passwords.
   
    [LMSTUDIO](https://lmstudio.ai)
    ```
       - Download llm models from lm studio these model run locally on your system.
       - llava-phi-3-mini-gguf  (intall vision adapter)  (image + text) model
       - NousResearch/Hermes-2-Pro-Mistral-7B-GGUF (install from lm studio for function calling)
    ````
    [WEATHER](https://rapidapi.com/weatherapi/api/weatherapi-com)
    ```
       - get weather api
    ```
    [NEWS](https://newsapi.org)
    ```
       - get news api
    ```
    [GMAIL_PASSWORD](https://myaccount.google.com/apppasswords)
    ```
       - generate password to send email using smptlib
    ```
5. **System requirements
    # higher is the specs better the model will perfomrm
   ```
    - 8gb+ ram (higher is better)
    - 250 gb+ storage 
    - i5 processor or m processor 
    - gpu / npu
   ```
  
   

## Installation
 
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ganeshnikhil/JARVIS.git
   cd JARVIS
   ```

2.**File structure**
```bash .
├── details.txt
├── main.py
├── src
│   ├── BRAIN
│   │   ├── func_call.py
│   │   ├── lm_ai.py
│   │   └── text_to_info.py
│   ├── CONVERSATION
│   │   ├── speech_to_text.py
│   │   ├── t_s.py
│   │   ├── test_speech.py
│   │   └── text_to_speech.py
│   ├── DATA
│   │   ├── email.py
│   │   ├── msg.py
│   │   └── tools.json
│   ├── FUNCTION
│   │   ├── Email_send.py
│   │   ├── ai_op.py
│   │   ├── app_op.py
│   │   ├── get_env.py
│   │   ├── greet_time.py
│   │   ├── incog.py
│   │   ├── link_op.py
│   │   ├── news.py
│   │   ├── random_respon.py
│   │   ├── run_function.py
│   │   ├── weather.py
│   │   └── youtube_downloader.py
│   ├── KEYBOARD
│   │   ├── key_lst.py
│   │   └── key_prs_lst.py
│   └── VISION
│       └── eye.py
└── tools.py

8 directories, 28 files
```
3. **Install Dependencies**:
   Install the required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Program**:
   Run the main Python script:
   ```bash
   python main.py
   ```

2. **Initial Interaction**:
   The assistant will greet you and explain how to interact with it. Example:
   ```
   [= =] Say 'hey jarvis' to activate, and 'stop' to deactivate. Say 'exit' to quit.
   ```

## Using the Assistant

### Starting a Conversation

- Say **"Hey Jarvis"** to activate the assistant.
- Jarvis will enter listening mode and wait for your commands.

### Giving Commands

- Speak clearly and concisely. For example:
  - **"What is the weather today?"**
  - **"Summarize the latest news."**
  - **"Draft an email."**

### Stopping Listening Mode

- Say **"Stop"** to deactivate listening mode.
- Jarvis will process the accumulated command text (if any) and stop listening for further input.

### Quitting the Application

- Say **"Exit"** to terminate the program. Jarvis will bid you goodbye before exiting.

## Error Handling

If an error occurs during execution, Jarvis will notify you with a polite message and log the issue for debugging purposes. Example:
```python
Error: [specific error message]
```

## Timeout Behavior

- If no commands are received for 5 minutes, listening mode will automatically deactivate, and Jarvis will notify you about the timeout.

## Example Workflow

1. Start the application with `python main.py`.
2. Jarvis greets you and waits for activation.
3. Say "Hey Jarvis" to activate.
4. Provide a command, e.g., "What's the weather like today?"
5. Jarvis responds with the summarized weather report.
6. Say "Stop" to end listening mode or "Exit" to quit the application.

## Transition to Function Calling Method

### Previous Similarity Score Method

Earlier implementations relied on similarity score-based methods to match user commands with pre-defined intents. While functional, this approach had limitations in handling diverse or complex queries effectively.

### Function Calling Using LLMs

Function calling is a modern approach leveraging the capabilities of Large Language Models (LLMs). It enables dynamic task execution by interpreting natural language inputs and mapping them to functions programmatically. This method is more adaptable and efficient for AI-driven applications.
Function calling enables developers to connect language models to external data and systems. You can define a set of functions as tools that the model has access to, and it can use them when appropriate based on the conversation history. You can then execute those functions on the application side, and provide results back to the model.

### Implementation Details

1. **Command Parsing**:
   - User input is parsed to identify the required function and arguments.
   - Example:
     ```python
     response = create_function_call(command)
     response_dic = parse_tool_call(response)
     ```

2. **Dynamic Function Execution**:
   - Identified functions are executed dynamically based on the parsed response.
   - Example:
     ```python
     if response_dic:
         func_name = response_dic["name"]
         response = execute_function_call(response_dic)
     ```

3. **Loading Messages**:
   - AI generates polite loading messages for a better user experience.
   - Example:
     ```python
     prompt = f"Generate a polite loading message for the function '{func_name}' less than 20 words."
     loading_message = send_to_ai(prompt)
     speak(loading_message)
     ```

4. **Error Handling**:
   - The system includes robust error handling to manage unexpected issues.
   - Example:
     ```python
     try:
         response = execute_function_call(response_dic)
     except Exception as e:
         speak("An unexpected error occurred. Please try again.")
         print(f"Error: {e}")
     ```

5. **Retry Mechanism**:
   - A retry mechanism ensures reliability when interacting with AI services.
   - Example:
     ```python
     def send_to_ai_with_retry(prompt, retries=3, delay=2):
         for _ in range(retries):
             try:
                 return send_to_ai(prompt)
             except Exception:
                 time.sleep(delay)
         speak("AI service is not responding. Please try again later.")
         return None
     ```

## Advantages of Function Calling

- Enhanced accuracy and flexibility in handling diverse queries.
- Reduced dependency on pre-defined intents.
- Scalable for adding new functionalities dynamically.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Follow these steps:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or feedback, please contact the project maintainer at [ganeshnikhil124@gmail.com].

