from django.contrib import admin

from .models import BasketballPlayer, BasketballTeam

# Register your models here.
admin.site.register(BasketballPlayer)
admin.site.register(BasketballTeam)
