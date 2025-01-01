import webbrowser 


def search_youtube(topic:str) -> None:
    format_topic = "+".join(topic.split())
    link = f"https://www.youtube.com/results?search_query={format_topic}"
    webbrowser.open(link)
    return None 

def open_youtube():
    link = f"https://www.youtube.com"
    webbrowser.open(link)
    return None 


def open_github():
    link = f"https://github.com"
    webbrowser.open(link)
    return None 

def yt_trending():
    link = f"https://www.youtube.com/feed/trending"
    webbrowser.open(link)
    return None 

def open_instagram():
    link = f"https://www.instagram.com"
    webbrowser.open(link)
    return None 


