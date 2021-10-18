from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome

