import json
import requests

with open('./model/testnum.json', 'rb') as f:
    prediction = requests.post('http://localhost:8180/predict', json=json.load(f))

if prediction.status_code == 200:
    prediction = json.loads(prediction.text)
    print(f'Prediction success: {prediction["success"]}\nPrediction is {prediction["predictions"]}')
else:
    print("response code is", prediction.status_code)
