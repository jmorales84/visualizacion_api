from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils.visualizacion import main

# Ruta para visualizar el dataset
@api_view(['GET'])
def visualizar_dataset(request):
    data = main()  # main() devuelve tu dataset en JSON
    return Response(data)
from django.http import JsonResponse

