from django.db import models

# Create your models here.
class Ruleset(models.Model):
    name=models.CharField(max_length='60',default='New App')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)
    update_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)

    class Meta:
        managed = False
        db_table = 'rulesets'