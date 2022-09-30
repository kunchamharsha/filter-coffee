from django.urls import path
from . import views



urlpatterns = [
    path("evaluate", views.evaluate_rules,name="evaluate"),
    path("list_tags", views.list_tags_view,name="list_tags"),
    path("", views.hello,name="evaluate"),
]
