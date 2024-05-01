```python
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, quote_plus

# Shared dependency
from utils.helpers import validate_input

class OSINTUtils:
    def __init__(self, api_key):
        self.api_key = api_key

    def gather_intelligence(self, target):
        validate_input(target)
        results = {}
        results['domain_info'] = self.get_domain_info(target)
        results['social_media'] = self.search_social_media(target)
        return results

    def get_domain_info(self, domain):
        # Use an external API to gather domain information
        url = f"https://api.domaininfo.com/v1/info?domain={quote_plus(domain)}&apiKey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to retrieve domain information"}

    def search_social_media(self, query):
        # Use an external API to search across social media platforms
        url = f"https://api.socialsearcher.com/v2/search?q={quote_plus(query)}&apiKey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to search social media"}

    def analyze_web_presence(self, target):
        # Scrape web presence information using BeautifulSoup
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(target, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return {
            "title": soup.title.string if soup.title else "No title found",
            "meta_description": soup.find("meta", attrs={"name": "description"})["content"] if soup.find("meta", attrs={"name": "description"}) else "No description found"
        }

    def perform_whois_lookup(self, domain):
        # Perform a WHOIS lookup to gather domain registration information
        url = f"https://api.whoislookup.com/v1/whois?domain={quote_plus(domain)}&apiKey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to perform WHOIS lookup"}

# Example usage:
# osint = OSINTUtils(api_key='YOUR_API_KEY')
# print(osint.gather_intelligence('example.com'))
```

This code provides a basic structure for the `utils/osint_utils.py` file, which includes functions to gather intelligence on a target domain, search social media, analyze web presence, and perform a WHOIS lookup. The `validate_input` function is assumed to be a shared dependency from `utils/helpers.py` that ensures the input is safe to use in queries. The actual API endpoints and keys are placeholders and should be replaced with real ones.