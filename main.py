import requests
from bs4 import BeautifulSoup

links = ""
nEpisodes = 292
# traverse paragraphs from soup
for i in range(1, nEpisodes):
    urls = 'https://dbzlatino.com/dragon-ball-z-capitulo-{}/'.format(i)
    grab = requests.get(urls)
    soup = BeautifulSoup(grab.text, 'html.parser')
    for cap in soup.find_all("iframe"):
        data = cap.get('src').replace("embed#!", "file/").replace("!", "#")
        links = links +"\n" + data
        print("Episode {}/{}".format(i, nEpisodes))

# opening a file in write mode
f = open("dbzlatino.txt", "w")
f.write(links)
f.close()
