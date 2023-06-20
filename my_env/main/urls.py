from django.urls import path
from .import views
from main.views import signup
from main.views import disclosures_view

app_name = "main"

urlpatterns = [
       path('', views.my_view, name='my-view'),
       path('unsubscribe', views.unsubscribe, name='unsubscribe'),
       path('signup/', views.signup, name='signup'),
       path('signup/success/', views.signup_success, name='signup_success'),
       
]