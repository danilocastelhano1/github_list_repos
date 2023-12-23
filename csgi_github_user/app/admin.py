from django.contrib import admin

from csgi_github_user.app.models import GitHubRepository


class GitHubRepositoryAdmin(admin.ModelAdmin):
    list_display = [
        "id", "user_name", "repo_name", "html_url", "description", "language"
    ]
    list_filter = [
        "user_name", "language"
    ]
    search_fields = [
        "id", "user_name", "repo_name", "html_url", "description", "language"
    ]


admin.site.register(GitHubRepository, GitHubRepositoryAdmin)
