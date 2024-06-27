import requests
from bs4 import BeautifulSoup
import json
import time

def extract_href_links(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to fetch the webpage. Status code: {response.status_code}")
            return []

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all h3 elements with the specified class
        h3_elements = soup.find_all('h3', class_='s-post-summary--content-title')
        
        # Extract href links from the anchor tags within the h3 elements
        href_links = []
        for h3 in h3_elements:
            anchor = h3.find('a')
            if anchor and 'href' in anchor.attrs:
                href_links.append("https://stackoverflow.com" + anchor['href'])
        
        return href_links
    except Exception as e:
        print(f"An error occurred while processing {url}: {str(e)}")
        return []

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

# Generate URLs
urls = [f"https://stackoverflow.com/questions/tagged/git?tab=votes&page={i}&pagesize=50" for i in range(1, 101)]

# Main execution
if __name__ == "__main__":
    all_links = []

    for url in urls:
        print(f"Processing: {url}")
        href_links = extract_href_links(url)
        all_links.extend(href_links)
        print(f"Found {len(href_links)} links on this page")
        
        # Add a small delay to avoid overwhelming the server
        time.sleep(1)

    # Save all links to JSON file
    json_filename = "all_href_links.json"
    save_to_json({"links": all_links}, json_filename)
    print(f"Extracted a total of {len(all_links)} links from {len(urls)} pages and saved them to {json_filename}")