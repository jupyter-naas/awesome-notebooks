import pandas as pd
import requests
import pydash as _pd
from urllib.parse import urlencode

class Github():
    @staticmethod
    def get_repository_url(url):
        return url.split("https://github.com/")[-1]
    
    def connect(self, token: str):
        # Init connect
        self.token = token
        
        # Init headers
        self.headers = {
            'Authorization': f'token {self.token}'
        }

        # Init end point
        self.repository = Repository(self.headers)

        # Set connexion to active
        self.connected = True
        return self


class Repository(Github):
    def __init__(self, headers):
        Github.__init__(self)
        self.headers = headers
        
    def get_commits(self, url):			
        """
        Return an dataframe object with 5 columns:
        - AUTHOR_NAME      object
        - AUTHOR_EMAIL     object
        - COMMIT_DATE      object
        - COMMIT_MESSAGE   object
        - COMMIT_ID        object

        Parameters
        ----------
        repository: str:
            Repository url from Github.
            Example : "https://github.com/jupyter-naas/awesome-notebooks"
            
        """
        # Get organisation and repository from url
        repository = Github.get_repository_url(url)
        
        # Get commits
        commits = []
        page = 1
        while True:
            params = {
                "state": "open",
                "per_page": "100",
                "page": page,
            }
            url = f"https://api.github.com/repos/{repository}/commits?{urlencode(params, safe='(),')}"
            res = requests.get(url, headers=self.headers)
            try:
                res.raise_for_status()
            except requests.HTTPError as e:
                raise(e)
            res_json = res.json()

            if len(res_json) == 0:
                break
            for r in res_json:
                commit = {
                    "AUTHOR_NAME": _pd.get(r, "author.login"),
                    "AUTHOR_EMAIL": _pd.get(r, "commit.author.email"),
                    "COMMIT_DATE": _pd.get(r, "commit.author.date").replace("T", " ").replace("Z", ""),
                    "COMMIT_MESSAGE": _pd.get(r, "commit.message"),
                    "COMMIT_ID": _pd.get(r, "sha"),
                }
                commits.append(commit)
            page += 1

        # Return dataframe
        df = pd.DataFrame(commits)
        df["COMMIT_DATE"] = pd.to_datetime(df['COMMIT_DATE'])
        return df