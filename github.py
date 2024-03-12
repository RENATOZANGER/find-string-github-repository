import os
import requests


class GitHubAPI:
    def __init__(self, token):
        self.headers = {"Authorization": f"Bearer {token}"}
    
    def search_code(self, owner, repo, string):
        url = f'https://api.github.com/search/code?q={string}+in:file+repo:{owner}/{repo}'
        response = requests.get(url, headers=self.headers, verify=False)
        
        if response.status_code == 200:
            result = response.json()
            for item in result['items']:
                print(f'File: {item["name"]}, URL: {item["html_url"]}')
                self._save_results(repo, item["html_url"], string)
        else:
            print(f'Error: {response.status_code}, {response.text}')
    
    def _save_results(self, repo, url, string):
        folder_path = f'Results-{repo}'
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(f'{folder_path}/{string}.txt', 'a') as file:
            file.write(f'{url}\n')
