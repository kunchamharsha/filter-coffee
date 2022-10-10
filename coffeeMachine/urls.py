from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from .services.users import UserService
from .services.apps import AppService
from .services.rules import RulesService
from .services.ruleset import RulesetService




routers = DefaultRouter()
routers.register('user', UserService, basename='user')
routers.register('app', AppService, basename='user')
routers.register('rules', RulesService, basename='user')
routers.register('ruleset', RulesetService, basename='user')



urlpatterns = [
    path("evaluate", views.evaluate_rules,name="evaluate"),
    path("list_tags", views.list_tags_view,name="list_tags"),
    path("", views.hello,name="evaluate"),
] + routers.urls
