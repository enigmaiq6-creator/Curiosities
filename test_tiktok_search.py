import requests
import re
import urllib.parse

def search_tiktok_yahoo_bing(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    
    # Test Yahoo Search
    yahoo_url = f"https://search.yahoo.com/search?p=site:tiktok.com/@+{urllib.parse.quote(query)}"
    try:
        r = requests.get(yahoo_url, headers=headers, timeout=5)
        links = re.findall(r'https%3a%2f%2fwww\.tiktok\.com%2f@[^/\\\'\"&%]+%2fvideo%2f\d+|https://(?:www\.)?tiktok\.com/@[^/\\\'\"&%]+/video/\d+', r.text, re.IGNORECASE)
        clean = list(set([urllib.parse.unquote(l) for l in links]))
        print(f"Yahoo found for '{query}':", len(clean), clean[:2])
    except Exception as e:
        print(f"Yahoo error: {e}")

    # Test Bing Search
    bing_url = f"https://www.bing.com/search?q=site%3Atiktok.com%2F%40+{urllib.parse.quote(query)}"
    try:
        r = requests.get(bing_url, headers=headers, timeout=5)
        links = re.findall(r'https://(?:www\.)?tiktok\.com/@[^/\\\'\"&%]+/video/\d+', r.text, re.IGNORECASE)
        clean = list(set(links))
        print(f"Bing found for '{query}':", len(clean), clean[:2])
    except Exception as e:
        print(f"Bing error: {e}")

if __name__ == "__main__":
    search_tiktok_yahoo_bing("pulpo nadando")
    search_tiktok_yahoo_bing("calamar gigante")
    search_tiktok_yahoo_bing("planeta venus")
