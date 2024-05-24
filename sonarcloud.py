# importing necessary libraries
from http.server import executable
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from sonarqube import SonarCloudClient
from sonarqube import SonarQubeClient
import sys
from config import SONARCLOUD_API_KEY, GITHUB_USERNAME, GITHUB_PASSWORD
sonar = SonarCloudClient(sonarcloud_url="https://sonarcloud.io", token=SONARCLOUD_API_KEY)

# Conducting code review in SonarCloud on all repositories 
def SonarAnalysis():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-gpu")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-dev-shm-usage')
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://sonarcloud.io/')
    githubclick = driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/div/div[2]/div[1]/div/div/div/a[1]')
    time.sleep(5)
    githubclick.click()
    time.sleep(5)
    githubusername = driver.find_element(By.XPATH, '//*[@id="login_field"]')
    githubusername.send_keys(GITHUB_USERNAME)
    githubpassword = driver.find_element(By.XPATH, '//*[@id="password"]')
    githubpassword.send_keys(GITHUB_PASSWORD)
    githubsigninclick = driver.find_element(By.XPATH, '//*[@id="login"]/div[3]/form/div/input[12]')
    githubsigninclick.click()
    time.sleep(5)
    plussign = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/nav/div/div/ul[1]/li[3]/button')
    plussign.click()
    analyzeprojects = driver.find_element(By.XPATH, '//*[@id="global-navigation"]/div/div/ul[1]/li[3]/div/ul/li[1]/a')
    analyzeprojects.click()
    time.sleep(5)
    selectallrepos = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div[1]/div/div[1]/a/i')
    selectallrepos.click()
    time.sleep(5)
    reposetup = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]/div/form/div[2]/div[2]/button')
    time.sleep(5)
    reposetup.click()
    time.sleep(300)
    driver.quit()
