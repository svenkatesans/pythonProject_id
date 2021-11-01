import requests

response = requests.get('https://api.github.com/users/svenkatesans/repos')
print('My GitHub repositories')
print('----------------------')
for repo in response.json():
    print('-' + repo['name'])
