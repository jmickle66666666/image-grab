import os, random
def rand_name():
    output = ''
    for i in range(10):
        output+=str(random.randint(0,9))
    return output

for i in range(20):
    print ("{}/20".format(i))
    os.system('python image_filter.py output/{}.png -s'.format(rand_name()))