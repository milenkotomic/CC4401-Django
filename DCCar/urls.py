from DCCar import views
from django.conf.urls import url

__author__ = 'milenkotomic'

app_name = 'DCCar'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<car_id>[0-9]+)/$', views.car_detail, name='car_detail'),
    url(r'^(?P<car_id>[0-9]+)/reserve/$', views.reserve, name='reserve'),
]