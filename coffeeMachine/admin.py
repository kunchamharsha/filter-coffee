from django.contrib import admin

# Register your models here.
from coffeeMachine.models import User,Ruleset,Rules,App
admin.site.register(User)
admin.site.register(Ruleset)
admin.site.register(Rules)
admin.site.register(App)
