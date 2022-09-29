from django.db import models
from coffeeMachine.model_data.ruleset import Ruleset

# Create your models here.
class Rules(models.Model):
    name=models.CharField(max_length=120,default='New App')
    description = models.TextField()
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)
    expression = models.TextField(blank=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)
    fields = models.JSONField()
    ruleset= models.ForeignKey(Ruleset,on_delete=models.CASCADE)
    weightage = models.IntegerField(default=0)
    payload = models.JSONField(null=True)
    class Meta:
        managed = True
        db_table = 'rules'