from django.conf.urls import url, include

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<pk>[0-9]+)/', include([
        url(r'^$', views.DetailView.as_view(), name='detail'),
        url(r'^results/$', views.ResultsView.as_view(), name='results'),
    ]))
]
