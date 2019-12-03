from django.db import models
from contacts.models import Client


class Service(models.Model):
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    name = models.CharField(verbose_name="Nome", max_length=200)
    description = models.CharField(verbose_name="Descrição",
                                   blank=True,
                                   null=True,
                                   max_length=200)
    price = models.FloatField(verbose_name="Preço")

    def __str__(self):
        return f'{self.name} - {self.price}'


class Product(models.Model):
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    name = models.CharField(verbose_name="Nome", max_length=200)
    description = models.CharField(verbose_name="Descrição",
                                   blank=True,
                                   null=True,
                                   max_length=200)
    price = models.FloatField(verbose_name="Preço")

    def __str__(self):
        return f'{self.name} - {self.price}'


class Invoice(models.Model):
    INVOICE_STATUSES = [
        ('PENDING', 'Pendente'),
        ('PAID', 'Paga'),
        ('CANCELED', 'Cancelada'),
        ('DRAFT', 'Rascunho'),
        ('PARTIALLY_PAID', 'Parcialmente Paga'),
    ]

    class Meta:
        verbose_name = "Fatura"
        verbose_name_plural = "Faturas"

    client = models.ForeignKey(Client,
                               verbose_name="Cliente",
                               on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Descrição",
                                   blank=True,
                                   null=True,
                                   max_length=200)
    status = models.CharField(max_length=50,
                              choices=INVOICE_STATUSES,
                              default=INVOICE_STATUSES[0])

    def __str__(self):
        return f'{self.name}'


class InvoiceProduct(models.Model):
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    amount = models.IntegerField(verbose_name="Quantidade")
    invoice = models.ForeignKey(Invoice,
                                verbose_name="Fatura",
                                on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                verbose_name="Produto",
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount}'


class InvoiceService(models.Model):
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    amount = models.IntegerField(verbose_name="Quantidade")
    invoice = models.ForeignKey(Invoice,
                                verbose_name="Fatura",
                                on_delete=models.CASCADE)
    service = models.ForeignKey(Service,
                                verbose_name="Serviço",
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount}'