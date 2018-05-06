from django.conf.urls import url
from . import views

# write your urls here
urlpatterns = [
    url(r'^$', views.index, name='index'),
]