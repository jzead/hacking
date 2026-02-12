import requests

url = "문제 주소/upload.php"

def upload_file(file_path):
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)

def get_response(file_name):
    response = requests.get(f"문제 주소/uploads/{file_name}")
    print('Get Response:', response.text)

upload_file("업로드 파일")
get_response("업로드 파일")