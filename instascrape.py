import requests
from bs4 import BeautifulSoup
import os
from instabot import Bot
import time
from random import seed
from random import randint
import shutil

try :
    shutil.rmtree('config')
except:
    pass

for f in os.listdir(r"C:\Users\mayma\OneDrive\Desktop\instascrape"):
        if(".jpeg" in f):
            os.remove(f)

urls = [
    'https://www.reddit.com/r/2meirl4meirl/top/',
    'https://www.reddit.com/r/meirl/top/',
    'https://www.reddit.com/r/2meirl42meirl4meirl/top/',
    'https://www.reddit.com/r/wholesomememes/top/',
    'https://www.reddit.com/r/LeopardsAteMyFace/top/',
    'https://www.reddit.com/r/HolUp/top/',
    'https://www.reddit.com/r/memes/top/',
    'https://www.reddit.com/r/suspiciouslyspecific/top/'
]

bot = Bot()
r = []

for url in urls:
    r.append(requests.get(url))

soup = []

for p in r:
    soup.append(BeautifulSoup(p.text, 'html.parser'))

for h in soup :
    print(h.title.text)

images = []

for image in soup:
    images.append(image.find_all('img'))

names = []
a = '1'

for image in images:
    for im in image :
        try :
            name = im['alt']
            link = im['src']
            if(name == "Post image"):
                print(link)
                with open(name + a + '.jpeg', 'wb') as f:
                    ima = requests.get(link)
                    f.write(ima.content)
                    names.append(name + a + '.jpeg')
                    a = str(int(a)+1)

        except KeyError:
            pass

print(names)
list = ["\U0001F610\nfollow @scrapertesterman\nfollow @scrapertesterman ",
        "\U0001F610\U0001F610\U0001F610\nfollow @scrapertesterman\nfollow @scrapertesterman",
        "\U0001F610\U0001F610\U0001F610\U0001F610\nfollow @scrapertesterman\nfollow @scrapertesterman ",
        "\U0001F610\U0001F610\U0001F610\U0001F610\U0001F610\nfollow @scrapertesterman\nfollow @scrapertesterman ",
        "\U0001F610\U0001F610\U0001F610\U0001F610\U0001F610\U0001F610\nfollow @scrapertesterman\nfollow @scrapertesterman " ,
        "\U0001F610\U0001F610\U0001F610\U0001F610\U0001F610\U0001F610\U0001F610\U0001F610\nfollow @scrapertesterman\nfollow @scrapertesterman"]

seed = int(input())

bot.login(username = "USER", password = "PWD")
for image in names:
        bot.upload_photo("./" + image,caption = list[randint(0,5)])
        time.sleep(300)
