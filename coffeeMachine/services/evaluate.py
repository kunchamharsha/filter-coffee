from re import I
from django.http import JsonResponse
from coffeeMachine.model_data.apps import App
from coffeeMachine.model_data.ruleset import Ruleset
from coffeeMachine.model_data.rules import Rules
from coffeeMachine.utils.custom_exceptions import MissingParamsForRuleEvaluation



def evaluate(service_id,params):
    service_id = App.objects.get(id=service_id)
    ruleset=Ruleset.objects.get(service=service_id,active=True)
    rules=Rules.objects.filter(ruleset=ruleset).all()
    eligible_rules=[]
    for rule in rules:
        try:
            if eval(rule.expression,params):
                eligible_rules.append(rule)
        except NameError:
            raise MissingParamsForRuleEvaluation
    sorted_rules = sorted(eligible_rules, key=lambda d: d.weightage) 
    payloads = [rule.payload for rule in sorted_rules]
    return payloads