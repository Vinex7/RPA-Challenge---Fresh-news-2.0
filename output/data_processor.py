# data_processor.py

def process_data(data):
    # Process the extracted data as needed
    # Example: Extract URLs from links
    extracted_urls = [link['href'] for link in data['links']]
    
    # Example: Extract text content from text elements
    text_content = [element.text for element in data['text_elements']]
    
    # Example: Process buttons or other elements
    processed_buttons = [button['name'] for button in data['buttons']]
    
    # Return the processed data
    return {"extracted_urls": extracted_urls, "text_content": text_content, "processed_buttons": processed_buttons}
