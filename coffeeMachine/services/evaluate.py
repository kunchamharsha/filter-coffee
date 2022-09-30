from re import I
from django.http import JsonResponse
from coffeeMachine.model_data.apps import App
from coffeeMachine.model_data.ruleset import Ruleset
from coffeeMachine.model_data.rules import Rules
from coffeeMachine.utils.custom_exceptions import MissingParamsForRuleEvaluation
from coffeeMachine.utils.validations import validate_input



def evaluate(service_id,params):
    service_id = App.objects.get(id=service_id)
    ruleset=Ruleset.objects.get(service=service_id,active=True)
    rules=Rules.objects.filter(ruleset=ruleset).all()
    eligible_rules=[]
    required_input_param_keys = []
    # if not validate_input({'required':required_input_param_keys,'given':params},'eval_params_check'):
    #     raise MissingParamsForRuleEvaluation
    for rule in rules:
        if eval(rule.expression,params):
            eligible_rules.append(rule)
    sorted_rules = sorted(eligible_rules, key=lambda d: d.weightage) 
    payloads = [rule.payload for rule in sorted_rules]
    return payloads