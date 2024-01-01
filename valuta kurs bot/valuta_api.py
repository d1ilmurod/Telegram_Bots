import requests
from pprint import pprint as print

API_KEY = '4b89a4df6a10917de87e71e0'
birlik = 'USD'

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{birlik}/UZS"

response = requests.get(url)
# print(response.status_code)
print(response.json())
# print(response.json()['conversion_rate'])
sana = response.json()['time_last_update_utc']
# print(f"Sana:{sana}")
kurs = response.json()['conversion_rate']
# print(f"1 dollar {kurs} so'mga teng")
# print(sana)
# print(kurs)
