import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/marketindex/').text
html = BeautifulSoup(response, 'html.parser')

print(html.select_one('#worldExchangeList > li:nth-child(3) > a.head.usd_gbp > div > span.value').text)

