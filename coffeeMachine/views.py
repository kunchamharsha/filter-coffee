from http import HTTPStatus
from signal import pause
from telnetlib import STATUS
from urllib import response
from django.forms import JSONField
from coffeeMachine.services.evaluate import evaluate,list_tags
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from coffeeMachine.utils.custom_exceptions import MissingParamsForRuleEvaluation
from coffeeMachine.utils.validations import validate_input
# Create your views here.
from django.http import HttpResponse, JsonResponse
# Create your views here.
import json

@require_http_methods(
    [
        "POST",
    ]
)
@csrf_exempt
def evaluate_rules(request):
    req_data = json.loads(request.body)
    input_params = req_data.get('input_params')
    service_id = req_data.get('service_id')
    print(input_params)
    print(service_id)
    if not validate_input(input_params,'input_params'):
        response = {
            'response':'invalid input_params'
        }
        return JsonResponse(response, content_type='application/json',status=417)
    if not validate_input(input_params,'service_id'):
        response = {
            'response':'invalid service_id'
        }
        return JsonResponse(response, content_type='application/json',status=417)

    try:
        payload = evaluate(service_id,input_params)
        return JsonResponse({'result':payload}, content_type='application/json')
    except MissingParamsForRuleEvaluation as e:
        response = {
            'response':'missing rules for evaluation, update service_params'
        }
        return JsonResponse(response,content_type='application/json',status=417)
    except Exception as e:
        return JsonResponse(str(e))

@require_http_methods(
    [
        "GET",
    ]
)
@csrf_exempt
def list_tags_view(request):
    service_id = request.GET.get('service_id')
    try:
        payload = list_tags(service_id)
        return JsonResponse({'result':payload}, content_type='application/json')
    except MissingParamsForRuleEvaluation as e:
        response = {
            'response':'missing rules for evaluation, update service_params'
        }
        return JsonResponse(response,content_type='application/json',status=417)
    except Exception as e:
        return JsonResponse(str(e))


@require_http_methods(
    [
        "POST",
    ]
)
@csrf_exempt
def hello():
    return "hello world"