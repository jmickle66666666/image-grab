from PIL import Image, ImageFilter, ImageChops
import image_grab, random, sys

verbose = True

def chops_filter(img):
    chops = ["invert","offset"]
    ch = random.choice(chops)
    if ch == "invert":
        return ImageChops.invert(img)
    if ch == "offset":
        return ImageChops.offset(img,random.randint(0,img.size[0]))

def pil_filter(img):
    filters = [ImageFilter.BLUR,ImageFilter.CONTOUR,ImageFilter.EDGE_ENHANCE,
                    ImageFilter.EDGE_ENHANCE_MORE,ImageFilter.EMBOSS,ImageFilter.FIND_EDGES,
                    ImageFilter.SMOOTH,ImageFilter.SMOOTH_MORE,ImageFilter.SHARPEN]
    flt = filters[random.randint(0,len(filters)-1)]
    if verbose: print(flt)
    return img.filter(flt)

def color_reduce_filter(img):
    return img.convert('P', dither=random.choice([Image.FLOYDSTEINBERG,Image.NONE]), palette=random.choice([Image.ADAPTIVE,Image.WEB]), colors=random.randint(2,16))

def resize_filter(img):
    os = img.size
    size = random.choice([64,128,256,300,400])
    sz = (size,size)
    if verbose: print(size)
    method = random.choice([Image.ANTIALIAS,Image.NEAREST])
    img = img.resize(sz, method)
    img = img.resize(os, method)
    return img

def filter(img):
    img = img.convert('RGB')
    ch = random.choice([pil_filter,resize_filter,color_reduce_filter,chops_filter])
    if verbose: print(ch)
    return ch(img)

def many_filters(img):
    runs = random.choice([6,7,8,9,20])
    if verbose: print("{} filters".format(runs))
    for i in range(runs):
        img = filter(img)
    return img

if __name__=="__main__":
    if len(sys.argv) > 2:
        if sys.argv[2] == "-s":
            verbose = False
    if verbose: print("filter")
    

    img = many_filters(image_grab.get_image("art deco","pixel","glitch","brutalist","vhs","hacker","gif","cat","dog","architecture","brutalism","jazz"))
    output_path = "output.png"
    if len(sys.argv) > 1:
        output_path = sys.argv[1]


    img = img.convert('RGB')
    img = img.thumbnail((400,400), Image.ANTIALIAS)

    img.save(output_path)