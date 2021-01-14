from django.forms import ModelForm
from .models import Dealer

class DealerForm(ModelForm):
    class Meta:
        model = Dealer
        fields = '__all__'
