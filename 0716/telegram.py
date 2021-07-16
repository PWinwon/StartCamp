import requests

#영어로 크롤링한 데이터를 매핑을 통해 한글로 번역하기 위한 딕셔너리
weather_mapping = {'Snow': '눈' ,'Sleet': '진눈깨비', 'Hail': '우박', 'Thunderstorm': '번개',\
    'Heavy Rain': '폭우', 'Light Rain': '이슬비', 'Showers': '소나기', 'Heavy Cloud' : '흐림',\
         'Light Cloud' : '흐린뒤 맑음', 'Clear': '맑음'}

location_url = 'https://www.metaweather.com/api/location/search/?query=seoul'
location = requests.get(location_url).json()


url_1 = 'https://www.metaweather.com/api/location/{}/2021/7/18/'.format(location[0]['woeid'])
response = requests.get(url_1).json()

weather_info = response[0]['weather_state_name']

for i in weather_mapping:
    if(i == weather_info):
        weather_info2 = weather_mapping[i]
        break


msg = f'서울의 모레 날씨는 {weather_info2}로 예상됩니다.'


TOKEN = '1817677668:AAHHNp0IE1RRrMpyFLXLGWUUaUiWriBSMpE'
url =f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1870231096&text={msg}"

response = requests.get(url).json

print(response)