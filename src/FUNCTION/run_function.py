from src.FUNCTION.link_op import search_youtube 
from src.FUNCTION.weather import weather_report
from src.FUNCTION.news import news_headlines
from src.FUNCTION.youtube_downloader import yt_download
from src.FUNCTION.app_op import app_runner
from src.FUNCTION.link_op import search_youtube , open_github , open_instagram , open_youtube , yt_trending
from src.BRAIN.text_to_info import send_to_ai 
from src.FUNCTION.incog import private_mode 
from src.FUNCTION.Email_send import send_email
from src.FUNCTION.phone_call import make_a_call
from typing import Union
FUNCTION_MAP = {
    'search_youtube': search_youtube,
    'weather_report': weather_report,
    'news_headlines':news_headlines,
    'yt_download':yt_download,
    'app_runner':app_runner,
    'open_github':open_github,
    'open_instagram':open_instagram,
    'open_youtube':open_youtube,
    'yt_trending':yt_trending,
    'send_to_ai':send_to_ai,
    'private_mode':private_mode,
    'send_email':send_email,
    'make_a_call':make_a_call
}


def execute_function_call(function_call: dict) -> Union[None,dict,list]:
    """
    Execute a function based on the function call dictionary
    
    :param function_call: Dictionary with 'name' and 'arguments' keys
    """
    output = None 
    try:
        # Extract function name and arguments
        func_name = function_call['name']
        args = function_call['arguments']
        keys = [args[k] for k in args.keys()]
        
        
        # Find the corresponding function
        func = FUNCTION_MAP.get(func_name)
        
        if func is None:
            print(f"No function found for {func_name}")
        
        if keys:
            # Call the function with unpacked arguments
            output = func(*keys)
            
        else:
            print("[*] No parameters provided .....")
            output = func()
    
    except KeyError as e:
        print(f"Invalid function call format: Missing {e}")
    except Exception as e:
        print(f"Error executing function: {e}")
    return output