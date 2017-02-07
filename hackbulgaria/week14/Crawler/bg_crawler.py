from bs4 import BeautifulSoup
import requests
url = 'http://register.start.bg/'
data = requests.get(url).content

page = BeautifulSoup(data,'html.parser')


statistics = {}

def link_gen():
    for l in page.findAll('a'):
        link = l.get('href')
        if link != None and 'link.php?' in link:
            yield link



for i in link_gen():
    try:
        s = requests.head(url+i, allow_redirects=True).headers.get('Server', 'Unknown')
        print(s)
        if s in statistics:
            statistics[s] += 1
        else:
            statistics[s] = 1
    except:
        print('error')
