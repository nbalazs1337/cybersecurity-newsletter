import requests



def get_feedly_data():
    #stream_id = 'feed/http://rss.packetstormsecurity.org/news/tags/zero_day/'  
    stream_id = 'feed/https://advisories.feedly.com/google/chrome/feed.json'
    count = 3
    url = f"https://cloud.feedly.com/v3/streams/contents?streamId={stream_id}&count={count}"
    access_token = "A8JCTCabGqCwwF3bAf2j_xHaE3fx52K_12RZ-fHzNfes0JGW5xvoYHTV7XBMmBhQ0noppF-pdgI4dExKDEUT0Mda4QhNUVlB5TjyRV6d1c-4NNCCgi75-Uhk_q2uw4Ar5X_rQsvipPNAtciO9rtm-LmP5AuvkKhEqYU4B0TyaCxqlO_gvfzuTLAhacfmHYwReFeOxKN4qfmoPoyGPHHn34KVuRw0O6o8kFoGAQUR3eR7wuq_W9XlXfxdj18:feedlydev"
    headers = {
        "Authorization": f"OAuth {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()
    #print(response.json())

#get_feedly_data()