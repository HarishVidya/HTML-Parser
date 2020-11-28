import requests
from bs4 import BeautifulSoup

def results(searchterm):
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

    name1_metro = soup_metro.find(class_="pt-title")
    name2_metro = name1_metro.findNext(class_="pt-title")
    name3_metro = name2_metro.findNext(class_="pt-title")
    name4_metro = name3_metro.findNext(class_="pt-title")

    price1 = price1_metro.text
    price2 = price2_metro.text
    price3 = price3_metro.text
    price4 = price4_metro.text

    name1 = name1_metro.text
    name2 = name2_metro.text
    name3 = name3_metro.text
    name4 = name4_metro.text

    return (price1, price2, price3, price4, name1, name2, name3, name4)

#if name1_metro and price1_metro:
 #   print('Metro:')
#if name1_metro and price1_metro:
 #   print(name1_metro.text + ' : ' + price1_metro.text)
#if name2_metro and price2_metro:
 #   print(name2_metro.text + ' : ' + price2_metro.text)
#if name3_metro and price3_metro:
 #   print(name3_metro.text + ' : ' + price3_metro.text)
#if name4_metro and price4_metro:
 #   print(name4_metro.text + ' : ' + price4_metro.text)


#print(soup_walmart.get_text())
#print(soup_superstore.prettify())
#price2_walmart = price1_walmart.findNext(class_="pi-price price-update")
#price3_walmart = price2_walmart.findNext(class_="pi-price price-update")
#price4_walmart = price3_walmart.findNext(class_="pi-price price-update")

#name1_walmart = soup_walmart.find(class_="pt-title")
#name2_walmart = name1_walmart.findNext(class_="pt-title")
#name3_walmart = name2_walmart.findNext(class_="pt-title")
#name4_walmart = name3_walmart.findNext(class_="pt-title")





#price1_superstore = soup_superstore.find(class_="product-name__item product-name__item--name")
#price2_superstore = price1_superstore.findNext(class_="product-name__item product-name__item--name")
#price3_superstore = price2_superstore.findNext(class_="product-name__item product-name__item--name")
#price4_superstore = price3_superstore.findNext(class_="product-name__item product-name__item--name")

#name1_superstore = soup_superstore.find(class_="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value")
#name2_superstore = name1_superstore.findNext(class_="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value")
#name3_superstore = name2_superstore.findNext(class_="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value")
#name4_superstore = name3_superstore.findNext(class_="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value")



#if name1_superstore and price1_superstore:
 #   print('Superstore:')
#if name1_superstore and price1_superstore:
 #   print(name1_superstore.text + ' : ' + price1_superstore.text)
#if name2_superstore and price2_superstore:
 #   print(name2_superstore.text + ' : ' + price2_superstore.text)
#if name3_superstore and price3_superstore:
 #   print(name3_superstore.text + ' : ' + price3_superstore.text)
#if name4_superstore and price4_superstore:
 #   print(name4_superstore.text + ' : ' + price4_superstore.text)
