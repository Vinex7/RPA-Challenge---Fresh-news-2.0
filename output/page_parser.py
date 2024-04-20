from bs4 import BeautifulSoup

def parse_page(page_content):
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Extract relevant data from the parsed page
    # Example: Find all links on the page
    links = soup.find_all('a')
    
    # Example: Find all text elements on the page
    text_elements = soup.find_all('p')
    
    # Example: Find buttons or other elements
    buttons = soup.find_all('button')
    
    # Return the extracted data
    return {"links": links, "text_elements": text_elements, "buttons": buttons}
