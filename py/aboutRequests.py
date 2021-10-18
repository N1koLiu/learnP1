import requests
from bs4 import BeautifulSoup

MyUa = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

r = requests.get('https://book.douban.com/subject/35519947/comments/', headers=MyUa)

soup = BeautifulSoup(r.text, "html5lib")

pattern = soup.find_all('span', 'short')

for i in pattern:
    print(i.string)
    print('\n')
