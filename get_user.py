import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://JIRA_DNS/rest/api/3/user/search/query"

auth = HTTPBasicAuth("USER", "TOKEN")

headers = {
   "Accept": "application/json"
}

query = {
   'query': 'is reporter of (KEY_PROJECT)'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))