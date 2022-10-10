from coffeeMachine.model_data.rules import Rules
from rest_framework import viewsets

from coffeeMachine.serializers import RulesSerializer

class RulesService(viewsets.ModelViewSet):
    model = Rules
    serializer_class = RulesSerializer
    queryset = Rules.objects.all()