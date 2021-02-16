import bs4
import requests

url = 'http://www.record.pt'
r = requests.get(url)
r_html = r.text

soup = bs4.BeautifulSoup(r_html,'html.parser')

#print(soup)

title = soup.find('title').string

titulos=soup.find_all(class_="eventAnalytics")
for t in titulos:
    print(t.text)
    

#print(titulos)