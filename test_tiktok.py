import urllib.request
import urllib.parse
import re
import requests
from typing import List

def search_tiktok_urls(keyword: str, max_results: int = 3) -> List[str]:
    """
    Busca videos de TikTok indexados por palabra clave.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    # 1. Búsqueda mediante DuckDuckGo HTML
    query = f"site:tiktok.com/@ {keyword}"
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    
    tiktok_urls = []
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=6) as response:
            html = response.read().decode("utf-8", errors="ignore")
            # Buscar enlaces a videos de TikTok (formato tiktok.com/@user/video/123456789)
            raw_links = re.findall(r'href=[\'"][^\'"]*?(https%3A%2F%2Fwww\.tiktok\.com%2F@[^/\'\"&%]+%2Fvideo%2F\d+|https?://(?:www\.)?tiktok\.com/@[^/\'\"]+/video/\d+)', html)
            
            for l in raw_links:
                clean_url = urllib.parse.unquote(l)
                if clean_url not in tiktok_urls:
                    tiktok_urls.append(clean_url)
                if len(tiktok_urls) >= max_results:
                    break
    except Exception as e:
        print(f"[TikTokSearch] Error en búsqueda: {e}")

    # Fallback con Bing si DuckDuckGo no devolvió suficientes
    if len(tiktok_urls) < max_results:
        try:
            bing_url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}"
            req = urllib.request.Request(bing_url, headers=headers)
            with urllib.request.urlopen(req, timeout=6) as response:
                html = response.read().decode("utf-8", errors="ignore")
                matches = re.findall(r'href=[\'"](https?://(?:www\.)?tiktok\.com/@[^/\'\"]+/video/\d+)', html)
                for m in matches:
                    if m not in tiktok_urls:
                        tiktok_urls.append(m)
                    if len(tiktok_urls) >= max_results:
                        break
        except Exception:
            pass

    return tiktok_urls

if __name__ == "__main__":
    test_keywords = ["pulpo nadando", "venus planeta espacio", "calamar gigante"]
    for kw in test_keywords:
        results = search_tiktok_urls(kw, max_results=2)
        print(f"Keywords: '{kw}' -> TikToks encontrados: {results}")
