from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Client, ClientWallet
from .forms import ClientForm, FundWalletForm
from rest_framework import generics
from .serializers import ClientSerializer, ClientDetailSerializer


class CreateClientView(generic.CreateView):
    form_class = ClientForm
    template_name = 'crm/create.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('crm:client_list')


class ListClientView(generic.ListView):
    queryset = Client.objects.all()
    template_name = 'crm/list.html'
    context_object_name = 'clients'


class DetailClientView(generic.DetailView):
    queryset = Client.objects.all()
    template_name = 'crm/detail.html'
    context_object_name = 'client'


class UpdateClientView(generic.UpdateView):
    model = Client
    form_class = ClientForm
    pk_url_kwarg = "pk"
    template_name = 'crm/update.html'
    context_object_name = 'update_client'
    # success_url: reverse('client_list')

    def get_success_url(self):
        return reverse('crm:client_detail', kwargs={"pk": self.kwargs["pk"]})


class DeleteClientView(generic.DeleteView):
    queryset = Client.objects.all()
    template_name = 'crm/delete.html'
    context_object_name = 'client'

    def get_success_url(self):
        return reverse('crm:client_list')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(DeleteClientView, self).post(request, *args, **kwargs)


class FundWalletView(generic.UpdateView):
    model = ClientWallet
    form_class = FundWalletForm
    pk_url_kwarg = "pk"
    template_name = "crm/fundwallet.html"
    context_object_name = "wallet"

    def get_success_url(self):
        return reverse("crm:client_list")


class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveAPIView):
    queryset = ClientWallet.objects.all()
    serializer_class = ClientDetailSerializer


def client_websocket(request, cid):
    client = get_object_or_404(Client, cid=cid)
    try:
        wallet = ClientWallet.objects.get(customer=client)
    except ObjectDoesNotExist:
        wallet = ClientWallet(client=client)
        wallet.save()

    return render(request, 'crm/websockets.html', 
                  {'client': client, 'wallet': wallet})
