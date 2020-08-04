import requests

url = 'https://beta.recommendations.unifiedlayer.com/users/121734/recommendations'

headers = {'referer': 'https://bluehost.com'}

response = requests.get(url, headers=headers)

print(f'status code: {response.status_code}')
