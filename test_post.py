import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'bat_team':'MI',
    'bowl_team':'CSK',
    'venue':'Eden Gardens',
    'batsman':'Player1',
    'bowler':'Player2',
    'runs':'50',
    'wickets':'2',
    'overs':'12.3',
    'striker':'30'
}

resp = requests.post(url, data=data)
print('STATUS', resp.status_code)
print(resp.text[:800])
