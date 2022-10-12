from dataclasses import field
from statistics import mode
from coffeeMachine.model_data.apps import App
from rest_framework import serializers
from coffeeMachine.model_data.users import User
from coffeeMachine.model_data.rules import Rules
from coffeeMachine.model_data.ruleset import Ruleset



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = '__all__'
        read_only_fields = ('id',)

class RulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rules
        fields = '__all__'
        read_only_fields = ('id',)

class RuleSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ruleset
        fields = '__all__'
        read_only_fields = ('id',)
