from django.db import models


class Service(models.Model):
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    name = models.CharField(verbose_name="Nome", max_length=200)
    description = models.CharField(verbose_name="Descrição",
                                   blank=True,
                                   null=True,
                                   max_length=200)
    price = models.FloatField()

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
    price = models.FloatField()

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

    name = models.CharField(verbose_name="Nome", max_length=200)
    description = models.CharField(verbose_name="Descrição",
                                   blank=True,
                                   null=True,
                                   max_length=200)
    status = models.CharField(max_length=50,
                              choices=INVOICE_STATUSES,
                              default=INVOICE_STATUSES[0])
    services = models.ManyToManyField(Service, verbose_name="Serviços")
    products = models.ManyToManyField(Product, verbose_name="Produtos")

    def __str__(self):
        return {self.name}
