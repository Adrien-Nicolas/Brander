import requests

url = 'http://127.0.0.1:8080/api/generate_design/'

data = {
    'text': 'A beautifull website to sell my ecological products',
    'mood': 'happy'
}


response = requests.post(url, data=data)

if response.status_code == 200:
    print(response.json())
else:
    print('Error:', response.content)
