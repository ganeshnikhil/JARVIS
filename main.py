import time
from src.FUNCTION.run_function import execute_function_call
from src.BRAIN.text_to_info import send_to_ai
from src.BRAIN.func_call import create_function_call, parse_tool_call
from src.CONVERSATION.speech_to_text import recognize_speech
from src.CONVERSATION.text_to_speech import speak
from src.FUNCTION.random_respon import random_choice
from src.FUNCTION.greet_time import time_of_day
from src.FUNCTION.Email_send import initate_email 
from src.DATA.msg import WELCOME_RESPONSES, END_RESPONSES, LISTENING_RESPONSES, NONLISTENING_RESPONSES

# Function to handle different tasks based on the function name
def task_action(function_name, response):
    if function_name == "send_to_ai":
        print(f"[= =] AI: \n{response}")
        speak(response)
        
    elif function_name == "weather_report":
        summarize_text = send_to_ai(f"{response} please summarize given data in less thand 20 words without using numerical data .")
        print(f"[= =] AI:\n {summarize_text}")
        speak(summarize_text)
    
    elif function_name == "news_headlines":
        if response:
            print("[= =] AI:\n")
            for headline in response:
                print(headline)
                speak(headline)
                print("\n\n")
                time.sleep(0.00001)
    
    elif function_name == 'send_email':
        subject = response.get('subject')  # Returns 30
        email_content = response.get('content')
        if subject and email_content:
            speak("The email has been drafted , ready to send now.")
            initate_email(subject , email_content)
        else:
            speak("An unexpected error occurred. Please try again.")
            print("Error occured Value error.")
    return None 


# Function to process commands and call the appropriate functions
def process_command(command):
    response = create_function_call(command)
    response_dic = parse_tool_call(response)
    print(response_dic)
    if response_dic:
        func_name = response_dic["name"]
        prompt = f"Generate a polite loading message for the function '{func_name}' less than 20 words."
        loading_message = send_to_ai(prompt)
        speak(loading_message)
        
        try:
            response = execute_function_call(response_dic)
            if response:
                task_action(func_name, response)
        except Exception as e:
            speak("An unexpected error occurred. Please try again.")
            print(f"Error: {e}")

# Function to handle retrying AI calls in case of failure
def send_to_ai_with_retry(prompt, retries=3, delay=2):
    for _ in range(retries):
        try:
            return send_to_ai(prompt)
        except Exception:
            time.sleep(delay)
    speak("AI service is not responding. Please try again later.")
    return None

# Main function to handle user interactions and speech recognition
def main():
    print("[= =] Say 'hey jarvis' to activate, and  'stop' to deactivate. Say 'exit' to quit.")
    listening_mode = False  # Track whether listening mode is active
    full_text = ""  # Store the user's spoken input
    speak(time_of_day())  # Greet the user based on the time of day
    speak(random_choice(WELCOME_RESPONSES))  # Welcome response
    last_speech_time = time.time()  # Track the last time speech was recognized
    timeout_duration = 300  # Timeout after 5 minutes of inactivity

    while True:
        spoken_text = recognize_speech()

        if not spoken_text:
            speak("Sorry, I couldn't hear that. Please try again.")
            continue
        
        spoken_text = spoken_text.lower().strip()
        print(f"You said: {spoken_text}")
        # If user says 'exit', terminate the program
        if spoken_text == "exit":
            print("[= =] Exiting...")
            speak(time_of_day())
            speak(random_choice(END_RESPONSES))  # Goodbye response
            break  

        # If 'hey jarvis' is detected, activate listening mode
        if "hey jarvis" in spoken_text:
            print("[+] Listening mode activated.")
            listening_mode = True
            speak(random_choice(LISTENING_RESPONSES))  # Respond when listening mode starts
            last_speech_time = time.time()  # Reset timeout on activation
            continue

        # If in listening mode, handle user commands
        if listening_mode:
            if "stop" in spoken_text:
                process_command(full_text)
                listening_mode = False  # Deactivate listening mode
                full_text = ""  # Reset full_text to empty
                print("[+] Listening mode deactivated.")
                speak(random_choice(NONLISTENING_RESPONSES))  # Response when stopping listening
                time.sleep(0.2)
            else:
                full_text += spoken_text + " "  # Append spoken text to full_text for command processing
                print(f"[*] Current text: {full_text}")

        # If the user has been inactive for too long, deactivate listening mode
        if time.time() - last_speech_time > timeout_duration and listening_mode:
            speak("Listening mode has timed out due to inactivity.")
            listening_mode = False
            full_text = ""  # Reset full_text
            print("[+] Listening mode deactivated.")
            speak(random_choice(NONLISTENING_RESPONSES))

if __name__ == "__main__":
    main()