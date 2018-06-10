from django.conf.urls import url
from apptwo import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
	path('',views.users,name='users'),
]