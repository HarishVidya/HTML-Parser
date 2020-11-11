import requests
from bs4 import BeautifulSoup

searchterm = input("What are you looking for? \n")

URL_metro = "https://www.metro.ca/en/search?filter=%s&freeText=true" % (searchterm)
URL_walmart = "https://www.walmart.ca/search?q=%s" % (searchterm)

page_metro = requests.get(URL_metro)
page_walmart = requests.get(URL_walmart)

soup_metro = BeautifulSoup(page_metro.content, 'html.parser')
soup_walmart = BeautifulSoup(page_walmart.content, 'html.parser')



price1_metro = soup_metro.find(class_="pi-price price-update")
price2_metro = price1_metro.findNext(class_="pi-price price-update")
price3_metro = price2_metro.findNext(class_="pi-price price-update")
price4_metro = price3_metro.findNext(class_="pi-price price-update")

#price1_walmart = soup_walmart.find(class_="css-1vsc4ug e175iya64")
#price2_walmart = price1_walmart.findNext(class_="css-2vqe5n esdkp3p0")
#price3_walmart = price2_walmart.findNext(class_="css-2vqe5n esdkp3p0")
#price4_walmart = price3_walmart.findNext(class_="css-2vqe5n esdkp3p0")

name1_metro = soup_metro.find(class_="pt-title")
name2_metro = name1_metro.findNext(class_="pt-title")
name3_metro = name2_metro.findNext(class_="pt-title")
name4_metro = name3_metro.findNext(class_="pt-title")

name1_walmart = soup_walmart.find(class_="css-1c6n0sl eudvd6x0")
#name2_walmart = name1_walmart.findNext(class_="css-1c6n0sl eudvd6x0")
#name3_walmart = name2_walmart.findNext(class_="css-1c6n0sl eudvd6x0")
#name4_walmart = name3_walmart.findNext(class_="css-1c6n0sl eudvd6x0")

if name1_metro and price1_metro:
    print('Metro:')
if name1_metro and price1_metro:
    print(name1_metro.text + ' : ' + price1_metro.text)
if name2_metro and price2_metro:
    print(name2_metro.text + ' : ' + price2_metro.text)
if name3_metro and price3_metro:
    print(name3_metro.text + ' : ' + price3_metro.text)
if name4_metro and price4_metro:
    print(name4_metro.text + ' : ' + price4_metro.text)

#if name1_walmart and price1_walmart:
    print(soup_walmart.prettify)
#if name1_walmart and price1_walmart:
   # print(name1_walmart.text + ' : ' + price1_walmart.text)
#if name2_walmart and price2_walmart:
 #   print(name2_walmart.text + ' : ' + price2_walmart.text)
#if name3_walmart and price3_walmart:
 #   print(name3_walmart.text + ' : ' + price3_walmart.text)
#if name4_walmart and price4_walmart:
 #   print(name4_walmart.text + ' : ' + price4_walmart.text)
