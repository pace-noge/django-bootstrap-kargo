from django.conf.urls import url
from . import views as vehicle_views


urlpatterns = [
    url(r'^$', vehicle_views.vehicle_list, name="index"),

    url(r'^create_vehicle/$', vehicle_views.create_vehicle, name="create_vehicle"),
    url(r'^edit_vehicle/(?P<pk>[0-9]+)/$', vehicle_views.edit_vehicle, name="edit_vehicle"),
    url(r'^delete_vehicle/(?P<pk>[0-9]+)/$', vehicle_views.delete_vehicle, name="delete_vehicle"),
]
