from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^details/(?P<image_id>[0-9]+)/$', views.details, name='details'),
    url(r'^about/$', views.about, name='about'),

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
