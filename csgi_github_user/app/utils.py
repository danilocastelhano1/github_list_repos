import requests

from typing import List
from typing import Tuple
from typing import Dict

from requests import Response

from csgi_github_user.app.models import GitHubRepository


class GithubRequest(object):
    def __init__(self, user_name: str) -> None:
        self.user_name = user_name
        self.github_repos_url = f"https://api.github.com/users/{self.user_name}/repos"
        self.max_repos_to_store = 5

    def get_repos_from_user_name(self) -> Tuple[GitHubRepository, Dict]:
        repos: GitHubRepository = self.__list_repos_from_user_name()
        if not repos:
            self.__get_repos_from_user_name_in_github()
            return self.__list_repos_from_user_name(), {"new_record": True}
        return repos, {"new_record": False}

    def __list_repos_from_user_name(self) -> GitHubRepository:
        return GitHubRepository.objects.filter(user_name=self.user_name)

    def __get_repos_from_user_name_in_github(self):
        response: Response = requests.get(self.github_repos_url)
        if response.ok:
            self.__insert_repos_in_db(repos=response.json())
        else:
            raise Exception("Error to make github request")

    def __insert_repos_in_db(self, repos: List) -> None:
        if not repos:
            return

        count: int = 0
        repos_to_add: List[GitHubRepository] = []

        for repo in repos:
            if count >= self.max_repos_to_store:
                break

            repos_to_add.append(
                GitHubRepository(
                    user_name=self.user_name,
                    repo_name=repo["name"] if repo["name"] else "No Name",
                    html_url=repo["html_url"] if repo["html_url"] else "No HTML",
                    description=repo["description"] if repo["description"] else "No Description",
                    language=repo["language"] if repo["language"] else "No Language"
                )
            )

            count += 1
        if repos_to_add:
            GitHubRepository.objects.bulk_create(repos_to_add)
