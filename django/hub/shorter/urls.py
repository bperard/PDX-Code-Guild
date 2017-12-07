from django.conf.urls import url

from . import views

app_name = 'shorter'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^entry/$', views.entry, name='entry'),
    url(r'^success/(?P<name>\w+)/(?P<long>.+)/$', views.success, name='success'),
    url(r'^(?P<search>.+)/$', views.go, name='go'),
]