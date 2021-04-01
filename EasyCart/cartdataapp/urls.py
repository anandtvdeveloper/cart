from django.urls import path
from cartdataapp import views
app_name='cartdataapp'

urlpatterns = [
    path('',views.allproduct,name='allproduct'),
    path('<slug:c_slug>/',views.allproduct,name='product_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.acpdetail,name='acpdetail'),
]