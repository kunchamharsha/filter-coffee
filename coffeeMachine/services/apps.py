from coffeeMachine.model_data.apps import App
from rest_framework import viewsets

from coffeeMachine.serializers import AppSerializer

class AppService(viewsets.ModelViewSet):
    model = App
    serializer_class = AppSerializer
    queryset = App.objects.all()