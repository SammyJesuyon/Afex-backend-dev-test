from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from .models import Client, ClientWallet
from .forms import ClientForm, FundWalletForm
from rest_framework import generics
from .serializers import ClientSerializer, ClientDetailSerializer


class CreateClientView(generic.CreateView):
    form_class = ClientForm
    template_name = 'client/create.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('crm:client_list')


class ListClientView(generic.ListView):
    queryset = Client.objects.all()
    template_name = 'client/list.html'
    context_object_name = 'clients'


class DetailClientView(generic.DetailView):
    queryset = Client.objects.all()
    template_name = 'client/detail.html'
    context_object_name = 'client'


class UpdateClientView(generic.UpdateView):
    model = Client
    form_class = ClientForm
    pk_url_kwarg = "pk"
    template_name = 'client/update.html'
    context_object_name = 'update_client'
    # success_url: reverse('client_list')

    def get_success_url(self):
        return reverse('crm:client_detail', kwargs={"pk": self.kwargs["pk"]})


class DeleteClientView(generic.DeleteView):
    queryset = Client.objects.all()
    template_name = 'client/delete.html'
    context_object_name = 'client'

    def get_success_url(self):
        return reverse('crm:client_list')


class FundWalletView(generic.UpdateView):
    model = ClientWallet
    form_class = FundWalletForm
    pk_url_kwarg = "pk"
    template_name = "client/fundwallet.html"
    context_object_name = "wallet"

    def get_success_url(self):
        return reverse("crm:client_list")
    

class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    

class ClientDetail(generics.RetrieveAPIView):
    queryset = ClientWallet.objects.all()
    serializer_class = ClientDetailSerializer


# def fund_wallet_view(request):
#     query_set = ClientWallet.objects.all()
#     form = FundWalletForm()
#     if request.method == 'POST':
#         form = FundWalletForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             print(form.errors)
#         return redirect('crm:client_list')
#     context = {'form': form, 'query_set': query_set}
#     return render(request, 'client/fundwallet.html', context)

# class FundWalletView(generic.UpdateView):
#     queryset = ClientWallet.objects.all() #look for a way to make pk=cid
#     # model = ClientWallet
#     form_class = FundWalletForm
#     template_name = 'client/fundwallet.html'
#     context_object_name = 'client_wallet'

#     def get_success_url(self):
#         return reverse('crm:client_list')
    # lookup_field = 'pk'
    # pk_url_kwarg = 'cid'

    # def get_queryset(self):
    #     return ClientWallet.objects.filter(customer__cid=int(self.kwargs['cid']))
    # success_url: reverse('client_list')

    # form_class = FundWalletForm
    # template_name = 'client/fundwallet.html'
    # queryset = ClientWallet.objects.all()

    # def get_queryset(self):
    #     wallet = self.queryset.get(id = 1)
    #     print(wallet)
    #     return wallet

    # def form_valid(self, form):
    #     form.save()
    #     return super(FundWalletView).form_valid(form)
