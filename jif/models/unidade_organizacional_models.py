from django.db import models


class UnidadeOrganizacional(models.Model):
    # Unidade Organizacional é ...
    #
    # UC02 - Manter Unidades Organizacionais:
    #     FA01 - Incluir Unidade Organizacional:
    #         2. O sistema apresenta os campos para entrada dos dados:
    #             - Nome (Obrigatório / Não se repete)

    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Unidade Organizacional'
        verbose_name_plural = 'Unidades Organizacionais'

    def __str__(self):
        return self.nome
