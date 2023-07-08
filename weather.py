import requests

# api_key = 'd4bf83539cae94b41e963098679d94e1'

# url = 'http://api.openweathermap.org/data/2.5/weather?q=hanoi&appid=d4bf83539cae94b41e963098679d94e1'

# res = requests.get(url)
# data = res.json()
# # print(data)
# description = data['weather'][0]['description']
# lon = data['coord']['lon']
# lat = data['coord']['lat']
# temp = data['main']['temp']
# humidity = data['main']['humidity']
# temp_celsius = int(temp)-272.15
# print('Nhiệt độ thành phố là: ',temp_celsius,'°C')
# print('Độ ẩm thành phố là: ',humidity,'%')

# city = input('Nhap thanh pho ban can tim: ')

def dubaothoitiet(city,api_key):
    # tim thanh pho
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key+''
    res = requests.get(url)
    data = res.json()

    # thong tin thanh pho
    description = data['weather'][0]['description']
    lon = data['coord']['lon'] #kinh do
    lat = data['coord']['lat'] #vi do
    temp = data['main']['temp'] #nhiet do F
    humidity = data['main']['humidity'] #do am
    temp_celsius = int(temp)-272.15  # doi ra do C  
    
    print('Nhiệt độ thành phố là: ',temp_celsius,'°C')
    print('Độ ẩm thành phố là: ',humidity,'%')

dubaothoitiet('hanoi','d4bf83539cae94b41e963098679d94e1')

