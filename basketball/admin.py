from django.contrib import admin
from django.db.models.fields.json import JSONField
from jsoneditor.forms import JSONEditor
from basketball.models import BasketballPlayer, BasketballTeam
from basketball.models import Voucher, VoucherReceipt
from basketball.models import UpgradeReceipt


# Custom admin class
class myAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {"widget": JSONEditor},
    }


# Register your models here.
admin.site.register(BasketballPlayer, myAdmin)
admin.site.register(BasketballTeam, myAdmin)
admin.site.register(Voucher, myAdmin)
admin.site.register(VoucherReceipt, myAdmin)
admin.site.register(UpgradeReceipt, myAdmin)
