from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length='60',default='New App')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)
    is_disabled=models.BooleanField(default=False)
    
    class Meta:
        managed = False
        db_table = 'users'