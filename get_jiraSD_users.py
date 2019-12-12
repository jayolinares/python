#!/bin/python3

## for reporting purposes.

import requests, json, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## by default, only active users are returned. 
url = 'https://jiraurl.local/jira/rest/api/2/user/search?username=@my_company.com&maxResults=50000'
headers = {'Content-Type': 'application/json',}

response = requests.get(url, headers=headers, auth=('MY_ID', 'MY_PASSWORD'), verify=False)
jira_sd = response.json()
output_file = open('/tmp/jiraSD.csv', 'w')
output_file.write("Username,Email Address,Name,Status" + "\n")

for users in jira_sd:
  try:
    fis_name = users['name']
    fis_email = users['emailAddress']
    fis_fullname = users['displayName']
    fis_status = users['active']
    jira_user = f"{fis_name},{fis_email},{fis_fullname},{fis_status}"
    output_file.write(jira_user + "\n")
  except:
    print("Error encountered.")

output_file.close()

