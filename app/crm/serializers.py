from .models import Client, ClientWallet
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        

class ClientDetailSerializer(serializers.ModelSerializer):
    client = ClientSerializer(source='customer')
    class Meta:
        model = ClientWallet
        fields = '__all__'
