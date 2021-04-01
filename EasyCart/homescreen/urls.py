from django.urls import path
from homescreen import views
app_name='homescreen'

urlpatterns = [
    path('',views.home,name='home'),
]
