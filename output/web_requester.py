import requests

def fetch_page(url):
    # Add a delay between requests to avoid being detected as a bot
    time.sleep(1)
    
    # Fetch the page content
    response = requests.get(https://www.aljazeera.com/)
    if response.status_code == 200:
        return response.text
    else:
        # Handle the error 
        print(f"Failed to fetch page: {https://www.aljazeera.com/}")
        return None
