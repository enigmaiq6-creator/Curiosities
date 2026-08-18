import requests
import re
import urllib.parse

def test_duckduckgo_raw(query):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    url = f"https://html.duckduckgo.com/html/?q=site:tiktok.com/@ {urllib.parse.quote(query)}"
    r = requests.get(url, headers=headers, timeout=6)
    print(f"Status: {r.status_code}, Length: {len(r.text)}")
    # Find uddg links
    uddg_links = re.findall(r'uddg=([^&"\']+)', r.text)
    decoded = [urllib.parse.unquote(l) for l in uddg_links if "tiktok.com" in urllib.parse.unquote(l)]
    print(f"Decoded DDG TikTok links for '{query}':", decoded[:3])
    return decoded

def test_tiktok_hashtag(tag):
    # Test yt-dlp on a tiktok search / hashtag
    import subprocess
    cmd = ["yt-dlp", f"https://www.tiktok.com/tag/{tag}", "--dump-json", "--flat-playlist", "--playlist-items", "1-2"]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    print(f"TikTok hashtag '{tag}' yt-dlp returncode: {res.returncode}")
    print(f"Output lines: {len(res.stdout.splitlines())}")
    for line in res.stdout.splitlines()[:2]:
        print(" ->", line[:100])

if __name__ == "__main__":
    test_duckduckgo_raw("pulpo nadando")
    test_duckduckgo_raw("calamar gigante")
    test_tiktok_hashtag("pulpo")
