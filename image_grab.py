import random, requests, pytumblr,json,os
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
    if len(j['response']) > 0:
        response = j["response"][random.randint(0,len(j['response'])-1)]
    else:
        return tumblr_image_search(search_term, life=life-1)

    if "photos" in response:
        if len(response['photos']) > 0:
            return response['photos'][random.randint(0,len(response['photos'])-1)]['original_size']['url']
        else:
            return tumblr_image_search(search_term, life=life-1)
    else:
        #print("no photos, retrying")
        return tumblr_image_search(search_term, life=life-1)
    
def dir_image():
    paths = [
    'C:/Users/jmickle/Dropbox/Public/gfx/2015/',
    'C:/Users/jmickle/Dropbox/Images/puushes/',
    r'C:\Users\jmickle\Dropbox\projects\games\2015\gloome\aqtx\aqtx\textures/'
    ]

    fls = []

    for path in paths:
        for file in os.listdir(path):
            if file.endswith(".png"):
                fls.append(path+file)

    sel = fls[random.randint(0,len(fls)-1)]

    return Image.open(sel)


def get_image(*args):
    func = random.choice(['dir','tumblr'])

    if func == 'dir':
        return dir_image()
    
    if func == 'tumblr':
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
