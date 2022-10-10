from coffeeMachine.model_data.ruleset import Ruleset
from rest_framework import viewsets

from coffeeMachine.serializers import RuleSetSerializer

class RulesetService(viewsets.ModelViewSet):
    model = Ruleset
    serializer_class = RuleSetSerializer
    queryset = Ruleset.objects.all()