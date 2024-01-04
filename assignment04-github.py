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

apikey = cfg["githubkey"]

g = Github(apikey)

repo = g.get_repo("SofiMetel/data-representation-coursework")
print(repo.clone_url)


fileInfo = repo.get_contents(filename)
urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile.replace("Andrew","Sofiia")
print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print (gitHubResponse)

