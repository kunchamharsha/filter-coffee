from coffeeMachine.model_data.users import User
from rest_framework import viewsets

from coffeeMachine.serializers import UserSerializer

class UserService(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
