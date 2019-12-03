from django.db import models
from places.models import Address


class Client(models.Model):
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    first_name = models.CharField(verbose_name="Primeiro Nome", max_length=200)
    middle_name = models.CharField(verbose_name="Nome do meio",
                                   blank=True,
                                   null=True,
                                   max_length=200)
    last_name = models.CharField(verbose_name="Último Nome", max_length=200)
    born_date = models.DateField(verbose_name="Data de Nascimento")
    rg = models.CharField(verbose_name="RG", max_length=14)
    cpf = models.CharField(verbose_name="CPF", max_length=11)
    address = models.ForeignKey(Address,
                                verbose_name="Endereço",
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)

    def __str__(self):
        if self.middle_name:
            return f'{self.first_name} {self.middle_name} {self.last_name}'
        return f'{self.first_name} {self.last_name}'


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
