import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'weight':55})

print(r.json())