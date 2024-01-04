import requests
import json
from config import config as cfg

from github import Github


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

#print (response.status_code)
#print (response.json())



#with  open(filename, 'w') as fp:
    #repoJSON = response.json()
    #json.dump(repoJSON, fp, indent=4)

if response.status_code == 200:
    # Extract the download URL for the file
    repo_json = response.json()
    file_contents_url = repo_json['contents_url'].replace('{+path}', filename)
    
    # Make a GET request to get the file content
    response = requests.get(file_contents_url, auth=('token', apikey))
    
    if response.status_code == 200:
        # Replace "Andrew" with your name in the file content
        file_content = response.json()['content']
        modified_content = file_content.replace("Andrew", "Sofiia")
        
        # Use PyGithub to commit changes back to the repository
        github = Github(apikey)
        repo = github.get_repo("SofiMetel/data-representation-coursework")
        file = repo.get_contents(filename)
        repo.update_file(file.path, "Update content", modified_content, file.sha)

        print("Changes committed and pushed.")
    else:
        print(f"Failed to retrieve file content. Status code: {response.status_code}")
else:
    print(f"Failed to retrieve repository information. Status code: {response.status_code}")

