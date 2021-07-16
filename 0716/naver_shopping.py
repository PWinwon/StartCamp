import requests
from pprint import pprint

query = '닌텐도스위치'
url = f'https://openapi.naver.com/v1/search/shop.json?query={query}'

head ={
    'X-Naver-Client-Id' : 'm_D3mWZfgTWFO04XPh6H',
    'X-Naver-Client-Secret' : 'SqXLhFeLVS'
}

response = requests.get(url, headers=head).json()

#pprint(response)

row_price = [0] * 10

for i in range(0,10):
    row_price[i] = int(response['items'][i]['lprice'])

#1 모든 가격 출력
print(row_price)

#2 최저가 출력
row_price.sort()
print(row_price[0])

#3 최저가명, 최저가, 최저가 쇼핑몰 링크
row_info = [0] * 2
for i in range(0,10):
    if (int(response['items'][i]['lprice']) == row_price[0]):
        row_info[0] = response['items'][i]['title']
        row_info[1] = response['items'][i]['link']
print(f'최저가명 : {row_info[0]}, 최저가 : {row_price[0]}, 링크 : {row_info[1]}')

#4 텔레그램으로 출력
msg = f'최저가명 : {row_info[0]}, 최저가 : {row_price[0]}, 링크 : {row_info[1]}'

TOKEN = '1817677668:AAHHNp0IE1RRrMpyFLXLGWUUaUiWriBSMpE'
url_t =f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1870231096&text={msg}"

response_t = requests.get(url_t).json
print(response_t)
