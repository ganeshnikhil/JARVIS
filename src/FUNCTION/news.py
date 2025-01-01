import requests
from src.FUNCTION.get_env import load_variable
# in , us 
def news_headlines( top = 10):
    api_key = load_variable("News_api")
    country = load_variable("Country")
    headlines = []
    url = ('https://newsapi.org/v2/top-headlines?'
        f'country={country}&'
        f'apiKey={api_key}')
    try:
        response = requests.get(url).json()
        all_articles = response['articles']
        total_results = int(response['totalResults'])
        for i in range(min(top , total_results)):
            headline = all_articles[i]['title']
            headlines.append(headline)
        return headlines
    except Exception as e:
        print(e)
        pass
    return None 

# api_key = "0ffa0913a62a413295e4efc23f37b1e1"
# headlines = news_headlines(api_key)
# print(headlines)


