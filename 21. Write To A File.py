#this is an extension to 17 Decode a Webpage. Here we save the results to a File

import bs4
import requests

url = 'http://www.record.pt'
r = requests.get(url)
r_html = r.text
soup = bs4.BeautifulSoup(r_html,'html.parser')
title = soup.find('title').string
titulos=soup.find_all(class_="noticia_box")
with open('record_headlines.txt', 'w') as open_file:
    for t in titulos:
        open_file.write(t.text)
    
        

