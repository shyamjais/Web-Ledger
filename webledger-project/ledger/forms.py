from django.forms import ModelForm
from .models import *

class LedgerForm(ModelForm):
    class Meta:
        model = Ledger
        fields = ['particulars', 'debit', 'credit', 'paymode', 'dr_cr', 'invoice', 'dealer', 'balance', 'collect_by']

        # def __init__(self, *args, **kwargs):
        #     super(LedgerForm, self).__init__(*args, **kwargs)
        #     print(kwargs)
        #     self.fields["dealer"] = kwargs["initial"]["dealer"].name
        #     self.fields["particulars"].initial = kwargs["initial"]["dealer"].name

class DealerForm(ModelForm):
    class Meta:
        model = Dealer
        fields = '__all__'


class RoadExpenseForm(ModelForm):
    class Meta:
        model = RoadExpense
        fields = '__all__'
