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

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class TipoModalidade(models.Model):
    # Tipo de Modalidade é ...
    #
    # UC11 – Manter Tipos de Modalidades:
    #     FA01 - Incluir Tipo de Modalidade:
    #         2. O sistema apresenta os campos para entrada dos dados:
    #             - Título (Obrigatório / Não se repete)

    titulo = models.CharField(max_length=100, unique=True, verbose_name='Título')

    class Meta:
        verbose_name = 'Tipo de Modalidade'
        verbose_name_plural = 'Tipos de Modalidades'

    def __str__(self):
        return self.titulo

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural
