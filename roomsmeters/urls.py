from django.urls import path
from . import views




urlpatterns = [

    path('', views.allmeters_list, name='index'),
    path('watermeter_create/', views.watermeter_create, name='watermeter_create'),
    path('rentaroom_create/', views.rentaroom_create, name='rentaroom_create'),
    path('electricitymeter_create/', views.electricitymeter_create, name='electricitymeter_create'),
    path('add_waterdata/', views.add_waterdata, name='add_waterdata'),
    path('add_electricitydate/', views.add_electricitydate, name='add_electricitydate'),
    path('outputmetersdata/', views.outputmetersdata, name='outputmetersdata'),

]