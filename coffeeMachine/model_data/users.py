from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=120,default='New App')
    profile_picture = models.TextField()
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, auto_now=False)
    is_disabled=models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'users'