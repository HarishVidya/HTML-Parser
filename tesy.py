import requests
from bs4 import BeautifulSoup

URL_walmart = "https://www.walmart.ca/search?q=onion"

page_walmart = requests.get(URL_walmart)

soup_walmart = BeautifulSoup(page_walmart.content, 'html.parser')

print(soup_walmart.get_text())
