from bs4 import BeautifulSoup

makeup ='<p class="comment-content"><span class="short">一般般吧</span></p>'

soup = BeautifulSoup(makeup, "html5lib")

print(soup)

print(soup.span)