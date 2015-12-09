import random, requests, pytumblr,json
from PIL import Image
from StringIO import StringIO

def tumblr_image_search(search_term):
    with open('client_keys.json') as data_file:    
        data = json.load(data_file)
    api_key = data['tumblr_api_key']

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
