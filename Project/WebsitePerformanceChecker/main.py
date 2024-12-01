import requests
import time
from bs4 import BeautifulSoup

def fetch_website(url):
    try:
        response = requests.get(url)
        return response
    except Exception as e:
        print(f"Error fetching website: {e}")
        return None

def measure_response_time(response):
    return response.elapsed.total_seconds()

def count_requests(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    num_requests = len(soup.find_all(['script', 'link', 'img', 'iframe', 'audio', 'video', 'source', 'track', 'embed', 'object', 'param']))
    return num_requests

def calculate_page_size(response):
    return len(response.content) / 1024  # Convert bytes to kilobytes

# You can add more functions to measure other metrics such as page load time, etc.

def check_website_performance(url):
    response = fetch_website(url)
    if response:
        response_time = measure_response_time(response)
        num_requests = count_requests(response)
        page_size = calculate_page_size(response)
        
        print(f"Response time: {response_time} seconds")
        print(f"Number of requests: {num_requests}")
        print(f"Page size: {page_size:.2f} KB")
    else:
        print("Failed to fetch website")

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    check_website_performance(website_url)
