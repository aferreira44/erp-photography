from django.contrib import admin
from django.db import models


class Address(models.Model):
    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    street = models.CharField(verbose_name="Logradouro", max_length=200)
    number = models.CharField(verbose_name="Número", max_length=20)
    complement = models.CharField(verbose_name="Complemento", max_length=200)
    postal_code = models.CharField(verbose_name="CEP", max_length=20)
    city = models.CharField(verbose_name="Cidade", max_length=200)
    state = models.CharField(verbose_name="Estado", max_length=200)

    def __str__(self):
        return f'{self.street}, {self.number} - {self.complement}'
