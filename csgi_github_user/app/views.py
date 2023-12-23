from django.shortcuts import render

from csgi_github_user.app.utils import GithubRequest


def index(request):
    if request.method == "GET":

        query = request.GET.get("q", None)
        if query:
            repos, _ = GithubRequest(query).get_repos_from_user_name()
            return render(request, "index.html", {
                "repos": repos,
                "query_value": "" if not query else query,
                "new_record": _["new_record"]
            })
        return render(request, "index.html", {})
