from src.FUNCTION.get_env import load_variable ,check_os
from os import system 


def start_app(path):
    os_name = check_os()
    if os_name == "Linux":
        system(f"{path}")
    elif os_name == "Darwin":
        system(f"open {path}")
    elif os_name == "Windows":
        system(f"start {path}")
    else:
        print("Invalid Operating sytem..")
        return False
    return True 
        
        
def app_runner(name):
    path = load_variable(name)
    flag = start_app(path)
    return flag 


