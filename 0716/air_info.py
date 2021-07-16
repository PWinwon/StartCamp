import requests

air_url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=강남구&dataTerm=month&returnType=json&pageNo=1&numOfRows=100&returnType=xml&serviceKey=stjlQoKqTsm4IBAGvPGwIa3rfwiC7FFtM9CkqUx7xxZInmSVJV09I8Fc9yPgArEEgkfnT%2BeSDxUg6uE6hp%2F7aA%3D%3D"

air_info = requests.get(air_url).json()

air_nano = air_info["response"]["body"]["items"][0]['pm10Value']
air_so2 = air_info["response"]["body"]["items"][0]['so2Value']
air_co = air_info["response"]["body"]["items"][0]['coValue']


msg = f'강남구의 미세먼지 농도는 {air_nano}, 아황산가스 농도는 {air_so2}, 일산화탄소 농도는 {air_co}입니다.'

TOKEN = '1817677668:AAHHNp0IE1RRrMpyFLXLGWUUaUiWriBSMpE'
url =f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1870231096&text={msg}"

response = requests.get(url).json

print(response)