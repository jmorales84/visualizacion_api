from django.urls import path
from .views import visualizar_dataset

urlpatterns = [
    path('api/visualizar/', visualizar_dataset, name='visualizar_dataset'),
]
