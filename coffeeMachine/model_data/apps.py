from django.db import models
from coffeeMachine.model_data.users import User

# Create your models here.
class App(models.Model):
    name=models.CharField(max_length=120,default='New App')
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)

    class Meta:
        managed = False
        db_table = 'apps'