import requests

kw = {'q': 'python'}
r = requests.get('http://cn.bing.com/search', params=kw)
print(r.text)