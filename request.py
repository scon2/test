import requests, json

# 요청을 보낼 URL
url = "http://127.0.0.1:8000/load-data/"
file_path = r"C:\Users\ChoJunseop\Downloads\processed_data (1).json"

#json 파일 열기
with open(file_path, 'r', encoding="UTF-8") as file:
    #파일 내용 읽기
    json_data = json.load(file)

# JSON 데이터를 포함하여 POST 요청 보내기
response = requests.post(url, json=json_data)

# 응답 받기
print(response.text)

