import requests
url = f"http://host8.dreamhack.games:22150/v2/signup"
res = requests.post(url,data={"username":"Admin","password":"1234"})
print(res.text)