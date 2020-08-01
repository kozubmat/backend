

from django.urls import path
from fleet.views import car_list, car_form

urlpatterns = [
    path('list/', car_list),
    path('add/', car_form),
    path('<int:pk>', car_form),
]
