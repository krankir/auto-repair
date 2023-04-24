from django.urls import path

from repairs.views import CreateRepair, ListRepair

app_name = 'repairs'

urlpatterns = [
    path('', ListRepair.as_view(), name='repairs'),
    path('create_repair/', CreateRepair.as_view(), name='create_repair'),
]