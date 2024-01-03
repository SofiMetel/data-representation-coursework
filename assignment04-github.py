import requests
import json
from config import config as cfg

'''
Write a program in python that will read a file from a repository, 
The program should then replace all the instances of the text "Andrew" with your name
The program should then commit those changes and push the file back to the repository.
I do not need to see your keys (see lab2, to follow)
Handup: Save the program as assignment04-github.py to the same repository you uploaded the xml to
Marks: Marks will be given for the functionality and layout of the code; I do expect minimal comments to indicate you know what the program is doing.
'''



filename = "fileandrew.txt"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://api.github.com/repos/SofiMetel/data-representation-coursework'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
print (response.json())

with  open(filename, 'w') as fp:
    #repoJSON = response.json()
    #json.dump(repoJSON, fp, indent=4)