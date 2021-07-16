import requests

location_url = 'https://www.metaweather.com/api/location/search/?query=seoul'
location = requests.get(location_url).json()


url = 'https://www.metaweather.com/api/location/{}/2021/7/18/'.format(location[0]['woeid'])
response = requests.get(url).json()

print('서울의 모레 날씨는 {}로 예상됩니다.'.format(response[0]['weather_state_name']))