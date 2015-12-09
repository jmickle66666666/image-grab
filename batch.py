import os, random, image_filter, image_grab
def rand_name():
    output = ''
    for i in range(10):
        output+=str(random.randint(0,9))
    return output

image_filter.verbose=False

words = ["art deco","pixel","glitch","brutalist","vhs","hacker","gif","cat","dog","architecture","brutalism","jazz",
"vaporwave","hyperwave","aloewave","classical","aesthetics","same","nsfw","landscape","horny","breasts","naked"]

for i in range(20):
    print ("{}/20".format(i+1))
    image_filter.many_filters(image_grab.get_image(*words)).save("output/{}.png".format(rand_name()))