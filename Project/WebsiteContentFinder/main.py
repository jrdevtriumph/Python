import requests
from bs4 import BeautifulSoup

def extract_text(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using Beautiful Soup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract all text from the parsed HTML
            text = soup.get_text()

            # Print the extracted text
            print(text)

        else:
            print(f"Error: {response.status_code} - {response.reason}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Enter the URL from which you want to extract text content
    url = input("Enter the URL: ")
    extract_text(url)