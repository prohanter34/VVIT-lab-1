import requests
apiKey = "c16a1d436e8a37d630f58618776b0216"
city = "Moscow"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': apiKey})
data=res.json()
print("Прогноз на день")
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Видимость:", data["visibility"])
print("Скорость ветра:", data["wind"]["speed"], " \r\n")

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': apiKey})
data = res.json()
print(res.text)
for i in data["list"]:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
          "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("____________________________")



