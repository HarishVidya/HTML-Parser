import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

searchterm = 'onion'

#URL_metro = "https://www.metro.ca/en/search?filter=%s&freeText=true" % (searchterm)
#URL_superstore = "https://www.realcanadiansuperstore.ca/search?search-bar=%s" % (searchterm)
URL_walmart = "https://www.walmart.ca/search?q=%s" % (searchterm)

browser = webdriver.Firefox()
browser.get(URL_walmart)
print (browser.title)
browser.quit()

#html = driver.page_source
#soup_walmart = BeautifulSoup(html)

#page_walmart = requests.get(URL_walmart)
#page_superstore = requests.get(URL_superstore)
#page_walmart = requests.get(URL_walmart)

#soup_walmart = BeautifulSoup(page_walmart.content, 'html.parser')
#soup_superstore = BeautifulSoup(page_superstore.content, 'html.parser')
#soup_walmart = BeautifulSoup(page_walmart.content, 'html.parser')

#price1_walmart = soup_walmart.find(class_="pi-price price-update")
#price2_walmart = price1_walmart.findNext(class_="pi-price price-update")
#price3_walmart = price2_walmart.findNext(class_="pi-price price-update")
#price4_walmart = price3_walmart.findNext(class_="pi-price price-update")

#name1_walmart = soup_walmart.find(class_="pt-title")
#name2_walmart = name1_walmart.findNext(class_="pt-title")
#name3_walmart = name2_walmart.findNext(class_="pt-title")
#name4_walmart = name3_walmart.findNext(class_="pt-title")

#price1 = price1_walmart.text
#price2 = price2_walmart.text
#price3 = price3_walmart.text
#price4 = price4_walmart.text

#name1 = name1_walmart.text
#name2 = name2_walmart.text
#name3 = name3_walmart.text
#name4 = name4_walmart.text

#print(soup_walmart.text)

#if name1_walmart and price1_walmart:
 #   print('Walmart:')
#if name1_walmart and price1_walmart:
 #   print(name1_walmart.text + ' : ' + price1_walmart.text)
#if name2_walmart and price2_walmart:
 #  print(name2_walmart.text + ' : ' + price2_walmart.text)
#if name3_walmart and price3_walmart:
 #  print(name3_walmart.text + ' : ' + price3_walmart.text)
#if name4_walmart and price4_walmart:
 #  print(name4_walmart.text + ' : ' + price4_metro.text)  