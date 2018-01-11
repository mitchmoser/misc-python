import requests
import sys
from bs4 import BeautifulSoup

url = sys.argv[1]

r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
page = soup.find_all('a')#(class_="content-section")

#print hyperlinks to other pages
#don't print links to sections of same page, etc
# example:  <a href='http*      = YES
#           <a href=#heading2  = NO
for link in page:
    L = str(link.get('href'))
    if L.startswith('http'):
        print(L)
