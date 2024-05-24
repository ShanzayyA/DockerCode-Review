
# GitHub + Docker Code Review / (Python)

This is a Docker app that uses SonarCloud and GitHub to do code reviews on all public repos for a given GitHub user. It takes a GitHub username, forks all the user's public repos, and checks them on SonarCloud to find bugs, code smells, and vulnerabilities.

## Installation

Before cloning the project, you need to create an App password if you haven't already. Go to Personal Settings and choose App passwords under Access Management. Click Create app password, name it whatever you like, select all Permissions, and click Create. Use this App password and your Bitbucket email to log in when cloning projects.

- Clone this repo

- Install Docker for your OS:

- `cd` into `container_content`, this folder has all the files and config to build the Docker image.

- Copy everything in `config.py.example` to a new `config.py` file and **edit** it to include your credentials. Follow these steps to get those credentials:

    - Go to [SonarCloud](https://sonarcloud.io/) and log in with your GitHub account. Click the "Account" icon on the top right, go to "My Account", select "Security" at the top, and create a new token. Name it anything you like. Copy this token and put it into `config.py` where it says `SONARCLOUD_API_KEY`.
    

    - Go to your GitHub account, click the icon at the top right, go to "Settings", then "Developer settings" on the bottom left, and select "Personal access tokens". Create a new token, name it anything you like, select all scopes, and set the expiration to "no expiration". Copy this token and put it into `config.py` where it says `GITHUB_API_KEY`.


    - In the `config.py` file, **edit** it to include your `GITHUB_USERNAME` and `GITHUB_PASSWORD` that you used to create the SonarCloud account and GitHub Personal access token.


- Build the image:

    ```sh
    docker build -t python_code_review .
    ```

- Check that the image was installed successfully:

    ```sh
    docker images
    ```

    It should list `python_code_review`.

- Run the image:

    ```sh
    docker run -i -t -d -p 8080:8080 --name python_code_review python_code_review
    ```

    The container should run the Python app at `http://localhost:8080`. Test with `curl -o - http://localhost:8080/<string:username>`.


- To stop the container:

    ```sh
    docker stop python_code_review
    ```

- To rebuild the container after making internal changes, run from `/container_content/`:

    ```sh
    docker stop python_code_review
    docker rmi python_code_review
    docker rm python_code_review
    docker rmi -f $(docker images -f "dangling=true" -q)
    docker build -t python_code_review .
    docker run -i -t -d -p 8080:8080 --name python_code_review python_code_review
    ```

## API Paths

### Username only

**GET /<string:username>**

