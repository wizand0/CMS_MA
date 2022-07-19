from django.urls import path
from . import views




urlpatterns = [

    path('', views.allmeters_list),
]