import requests
from bs4 import BeautifulSoup

def scrape_gumtree_search(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.prettify()

def main():
    item = input("Enter the item you want to search for: ")
    base_url = f'https://www.gumtree.com.au/s-{item}/k0r10'
    listings = scrape_gumtree_search(base_url)
    print(f'{listings}')

if __name__ == '__main__':
    main()

#This code also does not work as Gumtree blocks scraping attempts. The next step is to learn how to scrape ebay (due to its popularity) to familarize myself with scraping conventions.