from django.db import models
from django.db.models.signals import post_save


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Client(BaseModel):
    cid = models.CharField(max_length=60, unique=True, db_index=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(
        max_length=300, null=True, blank=True, default="")
    country_code = models.CharField(
        max_length=30, blank=True, null=True, default="")
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=50, null=True, blank=True, default="")

    class Meta:
        ordering = ['cid']

    def __str__(self):
        return f"{self.cid} - {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class ClientWallet(BaseModel):
    customer = models.OneToOneField(Client, related_name='clientwallet', on_delete=models.CASCADE, primary_key=True)
    total_balance = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    available_balance = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    lien_balance = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.cid} - {self.available_balance}"

    @property
    def cid(self):
        return self.customer.cid

def post_client_signal(sender, instance, created, **kwargs):
    if created:
        ClientWallet.objects.create(customer=instance)

post_save.connect(post_client_signal, sender=Client)