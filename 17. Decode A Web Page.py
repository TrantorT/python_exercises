import bs4
import requests

url = 'http://www.publico.pt'
r = requests.get(url)
r_html = r.text

soup = bs4.BeautifulSoup(r_html,'html.parser')

#print(soup)

title = soup.find('title').string

print(title)