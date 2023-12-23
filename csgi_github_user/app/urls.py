from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from csgi_github_user.app.views import index


urlpatterns = [
    path(r"", index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)