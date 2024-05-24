# importing necessary libraries
import github3
from github3 import login
from http.server import executable
import time
import sys
from config import GITHUB_API_KEY

# Login using a personal access token
github = github3.login(token=GITHUB_API_KEY)

# forking all public repositories for given user
def ForkRepos(username):
    for repository in github.repositories_by(username):
        repository.create_fork()
    time.sleep(5)
