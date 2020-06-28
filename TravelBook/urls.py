from django.urls import path
from . import views

app_name = 'Booking'
urlpatterns = [

    path('', views.index,name='index'),
    path('contect', views.contactus,name='contect'),
    path('search',views.fetchdata,name='search'),

]