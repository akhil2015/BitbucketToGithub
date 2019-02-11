import requests
import pprint
import json

api_url = 'https://api.bitbucket.org/2.0/repositories/'
user_name = 'shkshubham'
page_num = 1
clonable = []

## fetching all repositories using the bitbucket url
while True:
    raw_data = requests.get(api_url+user_name+'?page='+str(page_num))
    repo_data = json.loads(raw_data.text)['values']
    for repo in repo_data:
        if(repo['is_private']==False):
            clonable.append({'name':repo['full_name'],'clone':repo['links']['clone'][0]['href']})
    if('next' in json.loads(raw_data.text)):
        page_num = page_num+1
    else:
        break
for element in clonable:
    print(element['name'],end='\n')
print(str(len(clonable))+' public repositories found. Do you want to proceed (Y/n): ')

## creating the repositories in github using the github api


