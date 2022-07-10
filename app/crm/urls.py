from django import views
from django.urls import path
from .views import (
    CreateClientView, ListClientView, DetailClientView, UpdateClientView, DeleteClientView, FundWalletView
)

app_name = 'crm'

urlpatterns = [
    path('create/', CreateClientView.as_view(), name='create_client'),
    path('', ListClientView.as_view(), name='client_list'),
    path('detail/<int:pk>/', DetailClientView.as_view(), name='client_detail'),
    path('update/<int:pk>/', UpdateClientView.as_view(), name='client_update'),
    path('delete/<int:pk>/', DeleteClientView.as_view(), name='client_delete'),
    path('fundwallet/<int:pk>/', FundWalletView.as_view(), name='fund_wallet'),
]
