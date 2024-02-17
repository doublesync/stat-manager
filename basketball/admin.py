from django.contrib import admin
from django.db.models.fields.json import JSONField
from jsoneditor.forms import JSONEditor
from .models import BasketballPlayer, BasketballTeam


# Custom admin class
class myAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {"widget": JSONEditor},
    }


# Register your models here.
admin.site.register(BasketballPlayer, myAdmin)
admin.site.register(BasketballTeam, myAdmin)
