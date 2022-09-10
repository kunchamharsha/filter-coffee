from django.db import models
from coffeeMachine.model_data import ruleset

# Create your models here.
class Rules(models.Model):
    name=models.CharField(max_length='60',default='New App')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)
    expression = models.TextField(blank=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)
    fields = models.JSONField()
    ruleset= models.ForeignKey(ruleset)
    weightage = models.IntegerField(default=0)
    class Meta:
        managed = False
        db_table = 'rules'