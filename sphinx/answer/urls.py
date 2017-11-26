from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^answer/(?P<poll_id>\w{1,50})$', views.answer_page, name='answer_page'),
    url(r'^responses/(?P<poll_id>\w{1,50})$', views.responses_page, name='response_page'),
    url(r'^create$', views.create_page, name='create_page'),
]
