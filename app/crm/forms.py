from django.forms import ModelForm
from .models import Client, ClientWallet


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
class FundWalletForm(ModelForm):
    class Meta:
        model = ClientWallet
        fields = '__all__'
        exclude = ("customer",)