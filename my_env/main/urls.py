from django.urls import path
from .import views

app_name = "main"

urlpatterns = [
       path('', views.my_view, name='my-view'),
]

