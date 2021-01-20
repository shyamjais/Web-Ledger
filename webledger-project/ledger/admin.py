from django.contrib import admin
from .models import *

# Register your models here.
class LedgerAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    list_display = ('dealer','debit','credit','dr_cr','balance','dealer_ledger_number')


class ViewDealerAdmin(admin.ModelAdmin):
    filter_horizontal = ('dealer',)


admin.site.register(Dealer)
admin.site.register(Ledger, LedgerAdmin)
admin.site.register(Collected_by)
admin.site.register(ViewDealer, ViewDealerAdmin)
