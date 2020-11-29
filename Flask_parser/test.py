import requests
from bs4 import BeautifulSoup

searchterm = 'tomato'

URL_metro = "https://www.metro.ca/en/search?filter=%s&freeText=true" % (searchterm)
#URL_superstore = "https://www.realcanadiansuperstore.ca/search?search-bar=%s" % (searchterm)
#URL_walmart = "https://www.walmart.ca/search?q=%s" % (searchterm)

page_metro = requests.get(URL_metro)
#page_superstore = requests.get(URL_superstore)
#page_walmart = requests.get(URL_walmart)

soup_metro = BeautifulSoup(page_metro.content, 'html.parser')
#soup_superstore = BeautifulSoup(page_superstore.content, 'html.parser')
#soup_walmart = BeautifulSoup(page_walmart.content, 'html.parser')

price1_metro = soup_metro.find(class_="pi-price price-update")
price2_metro = price1_metro.findNext(class_="pi-price price-update")
price3_metro = price2_metro.findNext(class_="pi-price price-update")
price4_metro = price3_metro.findNext(class_="pi-price price-update")

if not price1_metro:
    price1_metro = soup_metro.find(class_="pi-price price-update pi-price-promo")

if not price2_metro:
    price2_metro = soup_metro.find(class_="pi-price price-update pi-price-promo")

if not price3_metro:
    price3_metro = soup_metro.find(class_="pi-price price-update pi-price-promo")

if not price4_metro:
    price4_metro = soup_metro.find(class_="pi-price price-update pi-price-promo")

name1_metro = soup_metro.find(class_="pt-title")
name2_metro = name1_metro.findNext(class_="pt-title")
name3_metro = name2_metro.findNext(class_="pt-title")
name4_metro = name3_metro.findNext(class_="pt-title")

#price1 = price1_metro.text
#price2 = price2_metro.text
#price3 = price3_metro.text
#price4 = price4_metro.text

#name1 = name1_metro.text
#name2 = name2_metro.text
#name3 = name3_metro.text
#name4 = name4_metro.text

if name1_metro and price1_metro:
    print('Metro:')
if name1_metro and price1_metro:
    print(name1_metro.text + ' : ' + price1_metro.text)
if name2_metro and price2_metro:
   print(name2_metro.text + ' : ' + price2_metro.text)
if name3_metro and price3_metro:
   print(name3_metro.text + ' : ' + price3_metro.text)
   print(name4_metro.text + ' : ' + price4_metro.text)  