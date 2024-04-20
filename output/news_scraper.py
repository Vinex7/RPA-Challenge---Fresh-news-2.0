import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
news_url = "https://www.aljazeera.com/"

# Send an HTTP GET request to the website
response = requests.get(news_url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find specific elements in the HTML content using BeautifulSoup
# For example, if you want to find all the headlines on the page:
headlines = soup.find_all('h2', class_='top-sec-title')

# Print out the headlines
for headline in headlines:
    print(headline.text.strip())

