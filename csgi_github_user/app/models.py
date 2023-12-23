from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GitHubRepository(BaseModel):
    user_name = models.CharField(blank=False, null=False, max_length=50)
    repo_name = models.CharField(blank=False, null=False, max_length=120)
    html_url = models.CharField(blank=False, null=False, max_length=1000)
    description = models.CharField(blank=False, null=False, max_length=255)
    language = models.CharField(blank=False, null=False, max_length=60)

    class Meta:
        verbose_name_plural = "GitHub Repositories"

    def __str__(self):
        return f"{self.user_name} - {self.repo_name} - {self.description}"
