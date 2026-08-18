import requests

def test_tikwm_search(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    url = "https://www.tikwm.com/api/feed/search"
    params = {
        "keywords": query,
        "count": 5,
        "cursor": 0,
        "web": 1
    }
    try:
        r = requests.post(url, data=params, headers=headers, timeout=6)
        print(f"TikWM Status for '{query}': {r.status_code}")
        data = r.json()
        videos = data.get("data", {}).get("videos", [])
        print(f"Found TikTok videos: {len(videos)}")
        for v in videos[:2]:
            title = v.get("title", "")
            play_url = v.get("play", "")
            wmplay = v.get("wmplay", "")
            duration = v.get("duration", 0)
            print(f" -> Title: {title[:50]} | Duration: {duration}s | Clean MP4 URL: {play_url[:60]}...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_tikwm_search("pulpo nadando")
    test_tikwm_search("calamar gigante")
    test_tikwm_search("planeta venus espacio")
