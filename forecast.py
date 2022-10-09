import requests

city = "Moscow,RU"
appid = "bde816a9134cfdfb0d91449aba12c8f8"

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

#print("Прогноз погоды на неделю:")
#for i in data['list']:
#    print('<Дата: ',i['dt_txt'], '>\r\nТемпература <',
#          i['main']['temp'], '>')


for i in data['list']:
    print("Дата <", i['dt_txt'],
          "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
          "> \r\nПогодные условия <", i['weather'][0]['description'],
          "> \r\nСкорость ветра <", i['wind']['speed'],
          "> \r\nВидимость <", i['visibility'] / 1000,"км >"
          )