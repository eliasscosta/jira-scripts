##  Remove all users from a group.
## https://developer.atlassian.com/cloud/jira/platform/rest/v3/#api-rest-api-3-group-user-delete


import requests
from requests.auth import HTTPBasicAuth
import json

## Change URL 
url_jira = "https://YOUR_JIRA"

get_users = url_jira + "/rest/api/3/group/member"
remove_users = url_jira + "/rest/api/3/group/user"

### Add group name
group = '{groupname}'

### set token api 
auth = HTTPBasicAuth("{email}", "{token-api}")

headers = {
"Accept": "application/json"
}

user = []

def get_user_from_group(url):

   query = {
      'groupname': group

   }

   r = requests.request(
      "GET",
      url,
      headers=headers,
      params=query,
      auth=auth
   )
   info = r.json()
   user.append(info.get('values'))
   if info.get('nextPage'):
      get_user_from_group(info['nextPage'])


def remove_users_from_group(url,accountId):

   query = {
   'groupname': group,
   'accountId': accountId
   }

   response = requests.request(
      "DELETE",
      url,
      params=query,
      auth=auth
   )
   print("{} - Status Code: {}".format(accountId,response.status_code))

get_user_from_group(get_users)

for i in range(0, len(user)):
   for k in range(0, len(user[i])):
      remove_users_from_group(remove_users,user[i][k]['accountId'])

## to running python3 ./jira.py