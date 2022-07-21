from django.urls import path
from . import views




urlpatterns = [

    path('', views.allmeters_list),
    path('watermeter_create/', views.watermeter_create, name='watermeter_create'),
    path('rentaroom_create/', views.rentaroom_create, name='rentaroom_create'),
]