from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^restaurants$', views.restaurants, name='restaurants'),
    url(r'^promotions/(?P<restaurant_id>\d+)/$', views.promotions, name='promotions'),#this uses a named group for regex
    url(r'^restaurant/add/$', views.RestaurantCreate.as_view(), name='restaurant-add'),
    url(r'^restaurant/(?P<pk>\d+)/$', views.RestaurantUpdate.as_view(), name='restaurant-update'),
    url(r'^ownerLogin$', views.ownerLogin, name ='ownerLogin'),
    url(r'^placefinder$', views.placefinder, name='placefinder'),
]
