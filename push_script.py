!pip install pygithub

from github import Github
import requests
import time

github = Github("aefcbe45583e1ee87ddea62bad904e4b095d1455")
def push(repo_path, file_path):
  filename = f"{time.time():.0f}.{file_path.split('.')[-1]}"
  github.get_repo('Scytheface/NARV').create_file(f"{repo_path}{filename}",
                   requests.get('http://whatthecommit.com/index.txt').text.strip(),
                   open(file_path, 'rb').read())