import bs4
import requests

url = 'http://www.publico.pt'
r = requests.get(url)
r_html = r.text

soup = bs4.BeautifulSoup(r_html,'html.parser')


#print(soup)

title = soup.find('title').string

titulos=soup.find_all(class_="card__title headline")
for t in titulos:
    print(t.find_all(class_="card__faux-block-link"))
    

#print(titulos)