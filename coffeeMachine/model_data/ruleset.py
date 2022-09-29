from django.db import models
from coffeeMachine.model_data.users import User
from coffeeMachine.model_data.apps import App

# Create your models here.
class Ruleset(models.Model):
    name=models.CharField(max_length=120,default='New App')
    description = models.TextField()
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)
    update_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey(App,on_delete=models.CASCADE,default=1)
    active = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'rulesets'