from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def scrape_page(search_term):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Set user agent to mimic a real browser
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        })

        url = f"https://www.gumtree.com.au/s-{search_term}/k0r10"
        print(f"Navigating to: {url}")

        page.goto(url)
        
        #Do not use in production, just for demo purposes
        page.wait_for_timeout(3000)  # Wait for 5 seconds to allow the page to load

        html = page.content()
        browser.close()

        soup = BeautifulSoup(html, 'html.parser')
        return soup

if __name__ == "__main__":
    soup = scrape_page("laptop")
    print(soup.prettify()[:1000])  # Print the first 1000 characters of the prettified HTML

# This approach is blocked by Gumtree and prevented by Facebook, so it may not work as expected.