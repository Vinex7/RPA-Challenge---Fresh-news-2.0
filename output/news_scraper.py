import requests
from bs4 import BeautifulSoup

news_url = "https://www.aljazeera.com/"

response = requests.get(news_url)
soup = BeautifulSoup(response.content, 'html.parser')

