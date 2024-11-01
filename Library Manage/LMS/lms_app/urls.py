from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(route="",view= home,name="home"),
    path(route="showbooks/",view= showbooks,name="showbooks"),
    path(route="deletebook/<int:id>",view= deletebook,name="deletebook"),
    path(route="updatebook/<int:id>",view= updatebook,name="updatebook",),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
