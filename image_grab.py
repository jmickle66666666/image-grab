import random, requests, pytumblr,json
from PIL import Image
from StringIO import StringIO

def tumblr_image_search(search_term, life=10):

    if life == 0: return None

    with open('client_keys.json') as data_file:    
        data = json.load(data_file)
    api_key = data['tumblr_api_key']

    url = 'http://api.tumblr.com/v2/tagged'

    r = requests.get(url,params={'tag':search_term,'api_key':api_key})

    j = r.json()

    response = j["response"][random.randint(0,len(j['response'])-1)]
    if "photos" in response:
        return response['photos'][random.randint(0,len(response['photos'])-1)]['original_size']['url']
    else:
        #print("no photos, retrying")
        return tumblr_image_search(search_term, life=life-1)
    

def get_image(*args):
    search_term = args[random.randint(0,len(args)-1)]
    url = tumblr_image_search(search_term)
    if url is not None:
        r = requests.get(url)
        i = Image.open(StringIO(r.content))
        return i
    else:
        return get_image(*args)

if  __name__=="__main__":
    get_image("brutalist").show()
