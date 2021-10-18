import requests
from bs4 import BeautifulSoup

MyUa = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

r = requests.get('https://www.coursera.org/learn/python-data-analysis/supplement/DNjE6/syllabus', headers=MyUa)

print(r.text)
