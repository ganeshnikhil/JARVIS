# JARVIS

# Jarvis AI Assistant

Welcome to the Jarvis AI Assistant project! This AI-powered assistant can perform various tasks such as providing weather reports, summarizing news headlines, sending emails, and more, all through voice commands. Below, you will find detailed instructions on how to set up, use, and interact with this application.

## Features

- **Voice Activation**: Say "Hey Jarvis" to activate listening mode.
- **Speech Recognition**: Recognizes and processes user commands via speech input.
- **AI Responses**: Provides responses using AI-generated text-to-speech output.
- **Task Execution**: Handles multiple tasks, including:
  - Sending emails.
  - Summarizing weather reports.
  - Reading news headlines.
  - General AI-based tasks.
  - Image generation.
  - Automate website and Applications.
  - Database functions.
  - Phone call automation using ADB.
- **Timeout Handling**: Automatically deactivates listening mode after 5 minutes of inactivity.
- **Automatic Input Processing**: If the user does not say "stop" within 60 seconds, the input is finalized and sent to the model for processing.
- **Multiple Function Calls**: Users can now call more than one function simultaneously, even if their inputs and outputs are unrelated.

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
3. **Setup the keys and passwords.**
   
    [LMSTUDIO](https://lmstudio.ai)
    ```
       - Download llm models from lm studio these model run locally on your system.
       - llava-phi-3-mini-gguf  (install vision adapter)  (image + text) model
       - NousResearch/Hermes-2-Pro-Mistral-7B-GGUF (install from lm studio for function calling)
    ```
    
    [WEATHER](https://rapidapi.com/weatherapi/api/weatherapi-com)
    ```
       - Get weather API
    ```
    [NEWS](https://newsapi.org)
    ```
       - Get news API
    ```
    [GMAIL_PASSWORD](https://myaccount.google.com/apppasswords)
    ```
       - Generate password to send email using smtplib
    ```

5. **System requirements**
   ```
    - 8GB+ RAM (higher is better)
    - 250GB+ storage 
    - i5 processor or M processor 
    - GPU / NPU
   ```

## Installation
 
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ganeshnikhil/JARVIS.git
   cd JARVIS
   ```

2. **Install Dependencies**:
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

## Transition in Function Calling Methods

### Previous Similarity Score Method

Earlier implementations relied on similarity score-based methods to match user commands with pre-defined intents. While functional, this approach had limitations in handling diverse or complex queries effectively.

### Shift to AI-Based Function Calling

To overcome these limitations, we transitioned to AI-powered function calling. Initially, we implemented a **single-function call** method, where AI models determined and executed one function at a time. Now, we have further improved the system by allowing **multiple function calls simultaneously**, enabling users to execute several commands at once, even if their inputs and outputs are unrelated. This enhancement significantly boosts efficiency and functionality.

### Model Performance

We are using the **Hermes-2-Pro-Mistral-7B-GGUF** model, which achieves **80-85% accuracy** on function-calling benchmarks (BFCL) and structured data processing. This improvement allows for more precise and structured output generation, making AI-driven interactions more reliable.

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

### ADB Installation & Setup

#### Install ADB on Windows, macOS, and Linux:
```bash
# Windows:
winget install --id=AndroidPlatformTools.AndroidPlatformTools

# macOS:
brew install android-platform-tools

# Linux (Debian/Ubuntu):
sudo apt install android-tools-adb
```

#### Enable Developer Options & Connect to ADB
1. **Enable Developer Mode on Phone:**
   - Go to **Settings > About Phone > Tap 'Build Number' 7 times**.
2. **Enable ADB Debugging:**
   - Go to **Settings > Developer Options > Enable USB Debugging & Wireless Debugging**.
3. **when you connect you device on a same network , the scirpt adb_connect.sh is there , that will automatically connect with the phone**
4. **It will try all sort of connections , and also store the new device_ip in device_ips.txt file**
5. **Also included method to try dirct using usb , then try for .venv , then try all saved device_ip in device_ips.txt file.**

### Manual method 
1. **Get Device IP & Connect via ADB:**
   ```bash
   adb tcpip 5555
   adb connect <device_ip>:5555
   ```
2. **USB Method:**
   ```bash
   adb devices
   adb shell ip -f inet addr show wlan0
   ```
   Update the `.env` file with the device IP.

### Contributing & License
For contributions, open a PR. This project is licensed under MIT.

## Contact
For any questions or feedback, please contact the project maintainer at [ganeshnikhil124@gmail.com].


