from django.urls import path
from . import views




urlpatterns = [

    path('/', views.electricitymeters_list),
]