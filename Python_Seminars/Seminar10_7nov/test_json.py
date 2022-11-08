import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# print(data['Valute']['USD'])
# print(data['Valute']['USD']['Nominal'])
# print(data['Valute']['USD']['Name'])
# print(data['Valute']['USD']['Value'])
nominal = data['Valute']['USD']['Nominal']
name = (data['Valute']['USD']['Name'])
value = data['Valute']['USD']['Value']
print(f'{nominal} {name} => {value}')