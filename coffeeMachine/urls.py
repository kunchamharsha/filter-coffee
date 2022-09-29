from django.urls import path
from . import views



urlpatterns = [
    path("evaluate", views.evaluate_rules,name="evaluate"),
    path("", views.hello,name="evaluate"),
]
