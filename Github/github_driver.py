import pandas as pd
import requests
import pydash as _pd
from urllib.parse import urlencode


class Github:
    @staticmethod
    def get_repository_url(url):
        return url.split("https://github.com/")[-1]

    def connect(self, token: str):
        # Init connect
        self.token = token

        # Init headers
        self.headers = {"Authorization": f"token {self.token}"}

        # Init end point
        self.repos = Repositories(self.headers)

        # Set connexion to active
        self.connected = True
        return self


class Repositories(Github):
    def __init__(self, headers):
        Github.__init__(self)
        self.headers = headers

    def get_commits(self, url):
        """
        Return an dataframe object with 11 columns:
        - ID                   object
        - MESSAGE              object
        - AUTHOR_DATE          date
        - AUTHOR_NAME          object
        - AUTHOR_EMAIL         object
        - COMMITTER_DATE       date
        - COMMITTER_NAME       object
        - COMMITTER_EMAIL      object
        - COMMENTS_COUNT       int
        - VERIFICATION_REASON  object
        - VERIFICATION_STATUS  object

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
                raise (e)
            res_json = res.json()

            if len(res_json) == 0:
                break
            for r in res_json:
                commit = {
                    "ID": _pd.get(r, "sha"),
                    "MESSAGE": _pd.get(r, "commit.message"),
                    "AUTHOR_DATE": _pd.get(r, "commit.author.date")
                    .replace("T", " ")
                    .replace("Z", ""),
                    "AUTHOR_NAME": _pd.get(r, "commit.author.name"),
                    "AUTHOR_EMAIL": _pd.get(r, "commit.author.email"),
                    "COMMITTER_DATE": _pd.get(r, "commit.committer.date")
                    .replace("T", " ")
                    .replace("Z", ""),
                    "COMMITTER_NAME": _pd.get(r, "commit.committer.name"),
                    "COMMITTER_EMAIL": _pd.get(r, "commit.committer.email"),
                    "COMMENTS_COUNT": _pd.get(r, "commit.comment_count"),
                    "VERIFICATION_REASON": _pd.get(r, "commit.verification.reason"),
                    "VERIFICATION_STATUS": _pd.get(r, "commit.verification.verified"),
                }
                commits.append(commit)
            page += 1
        # Return dataframe
        df = pd.DataFrame(commits)
        df["AUTHOR_DATE"] = pd.to_datetime(df["AUTHOR_DATE"])
        df["COMMITTER_DATE"] = pd.to_datetime(df["COMMITTER_DATE"])
        return df
    
    def get_stargazers(self, url):
        """
        Return an dataframe object with 6 columns:
        - LOGIN       object
        - ID          int64
        - URL         object
        - TYPE        object
        - SITE_ADMIN  bool
        - STARRED_AT  object

        Parameters
        ----------
        repository: str:
            Repository url from Github.
            Example : "https://github.com/jupyter-naas/awesome-notebooks"
        """
        # Get organisation and repository from url
        repository = Github.get_repository_url(url)
        
        # Custom headers
        headers = self.headers
        headers['Accept'] = 'application/vnd.github.v3.star+json'
        
        df = pd.DataFrame()
        page = 1
        while True:
            params = {
                "per_page": "100",
                "page": page,
            }
            url = f"https://api.github.com/repos/{repository}/stargazers?{urlencode(params, safe='(),')}"
            res = requests.get(url, headers=headers)
            try:
                res.raise_for_status()
            except requests.HTTPError as e:
                raise(e)
            res_json = res.json()

            if len(res_json) == 0:
                break
            for json in res_json:
                starred_at = json.get("starred_at")
                user = json.get("user")
                tmp = pd.DataFrame([user])
                tmp["starred_at"] = starred_at
                df = pd.concat([df, tmp], axis=0)
            page += 1
    
        # Cleaning
        for col in df.columns:
            if col.endswith("_url") or col.endswith("_id"):
                df = df.drop(col, axis=1)
            if col.endswith("_at"):
                df[col] = df[col].str.replace("T", " ").str.replace("Z", " ")
        df.columns = df.columns.str.upper()
        return df