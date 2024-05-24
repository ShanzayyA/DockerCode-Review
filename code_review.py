# importing necessary libraries
from sonarqube import SonarCloudClient
from sonarqube import SonarQubeClient
import sys
from http.server import executable
from config import SONARCLOUD_API_KEY
sonar = SonarCloudClient(sonarcloud_url="https://sonarcloud.io", token=SONARCLOUD_API_KEY)


def GetCodeReview():
    analyzed_repos = list(sonar.favorites.search_favorites())
    analyzed_repo_list = []
    for i in range(len(analyzed_repos)):
        repos = analyzed_repos[i]
        analyzed_repo_list.append(repos["key"])

    repo_review = {}
    for repo_name in analyzed_repo_list:
        analysis = list(sonar.issues.search_issues(componentKeys=repo_name))
        a = {}
        for i in range(len(analysis)):
            item = analysis[i]
            if item["author"] in a:
                a[item["author"]][item["type"]] = a[item["author"]][item["type"]] + 1                
            else:
                a[item["author"]] = {"BUG":0, "CODE_SMELL":0, "VULNERABILITY":0}
                a[item["author"]][item["type"]] = 1      
        repo_review[repo_name] = a
    return repo_review