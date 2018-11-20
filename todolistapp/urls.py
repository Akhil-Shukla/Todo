from . import views
from django.conf.urls import url

urlpatterns=[
    url('^index/',views.index),
    url('^edit/', views.edit),
    url('^update/', views.update),
    url('^remove/', views.remove),
    url('^api/',views.api)

]