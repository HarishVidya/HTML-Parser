import requests
from bs4 import BeautifulSoup

searchterm = input("What are you looking for? \n")

URL_metro = "https://www.metro.ca/en/search?filter=%s&freeText=true" % (searchterm)
URL_superstore = "https://www.realcanadiansuperstore.ca/search?search-bar=%s" % (searchterm)


page_metro = requests.get(URL_metro)
page_superstore = requests.get(URL_superstore)


soup_metro = BeautifulSoup(page_metro.content, 'html.parser')
soup_superstore = BeautifulSoup(page_superstore.content, 'html.parser')


price1_metro = soup_metro.find(class_="pi-price price-update")
price2_metro = price1_metro.findNext(class_="pi-price price-update")
price3_metro = price2_metro.findNext(class_="pi-price price-update")
price4_metro = price3_metro.findNext(class_="pi-price price-update")

price1_superstore = soup_superstore.find(class_="product-name__item product-name__item--name")
#price2_superstore = price1_superstore.findNext(class_="product-name__item product-name__item--name")
#price3_superstore = price2_superstore.findNext(class_="product-name__item product-name__item--name")
#price4_superstore = price3_superstore.findNext(class_="product-name__item product-name__item--name")

name1_metro = soup_metro.find(class_="pt-title")
name2_metro = name1_metro.findNext(class_="pt-title")
name3_metro = name2_metro.findNext(class_="pt-title")
name4_metro = name3_metro.findNext(class_="pt-title")

name1_superstore = soup_superstore.find(class_="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value")
#name2_superstore = name1_superstore.findNext(class_="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value")
#name3_superstore = name2_superstore.findNext(class_="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value")
#name4_superstore = name3_superstore.findNext(class_="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value")


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

if name1_superstore and price1_superstore:
    print('Superstore:')
if name1_superstore and price1_superstore:
    print(name1_superstore.text + ' : ' + price1_superstore.text)
#if name2_superstore and price2_superstore:
 #   print(name2_superstore.text + ' : ' + price2_superstore.text)
#if name3_superstore and price3_superstore:
 #   print(name3_superstore.text + ' : ' + price3_superstore.text)
#if name4_superstore and price4_superstore:
 #   print(name4_superstore.text + ' : ' + price4_superstore.text)
