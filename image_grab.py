import random, requests, pytumblr
from PIL import Image
from StringIO import StringIO

def tumblr_image_search(search_term):
    api_key = '6xqaiTlHrTb8H3fesP1ulOgM90YE0lZlUlyi4vQEjGPOPScSfq'
    client = pytumblr.TumblrRestClient(
      '6xqaiTlHrTb8H3fesP1ulOgM90YE0lZlUlyi4vQEjGPOPScSfq',
      'zuDWY12WIu9pGsrY9BgqONxGzfwRrz1yhzwKe0YDVyMqZa3oX4',
      'RnlGq73Shc5idVeD5eDjOtENPV87DpMA7hhw5BWKsvtV2Z0HnE',
      'lqA3owfHGzM6HVz0GIhvdtBjskyczwH6UbUZyojIC0p3ZkRFzr'
    )

    url = 'http://api.tumblr.com/v2/tagged'

    r = requests.get(url,params={'tag':search_term,'api_key':api_key})

    #url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=fuzzy%20monkey'
    #r = requests.get(url)
    j = r.json()

    response = j["response"][random.randint(0,len(j['response'])-1)]
    if "photos" in response:
        return response['photos'][random.randint(0,len(response['photos'])-1)]['original_size']['url']
    else:
        print("no photos, retrying")
        return tumblr_image_search(search_term)
    

def get_image(*args):
    search_term = args[random.randint(0,len(args)-1)]
    url = tumblr_image_search(search_term)
    r = requests.get(url)
    i = Image.open(StringIO(r.content))
    i.show()

if  __name__=="__main__":
    get_image("brutalist")