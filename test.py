import requests
import json
r = requests.post('https://api.keksik.io/balance', data=json.dumps({
    'group': 198161648,
    'token': '5bd2a48b3adcf65fba1300339a082825012c00847c5fd46e77',
    'v': 1
}), headers={
    'Content-type': 'application/json'
})
print(r.text)