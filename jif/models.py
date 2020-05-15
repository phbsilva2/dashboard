from django.db import models
from stdimage.models import StdImageField


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


class Modalidade(models.Model):
    # Modalidade é ...
    #
    # UC03 - Manter Modalidades
    #     FA01 - Incluir Modalidade
    #         2. O sistema apresenta os campos para entrada dos dados:
    #             - Nome (Obrigatório / Não se repete)
    #             - Sigla (Obrigatório / Não se repete)
    #             - Tipo (Obrigatório) [IndividuaL/Coletivo]
    #             - Tipo de Modalidade (Obrigatório)
    #
    # UC04 - Manter Atletas por Modalidade
    #     FA01 - Incluir Atleta por Modalidade
    #         2. O sistema apresenta os campos para entrada dos dados:
    #             - Modalidade (Obrigatório / Não se repete)
    #             - Lotação Permitida (Obrigatório / Não se repete)

    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=1, choices=[['I', 'Individual'], ['C', 'Coletivo']])
    tipo_modalidade = models.ForeignKey(TipoModalidade, on_delete=models.CASCADE, verbose_name='Tipo de Modalidade')
    lotacao_permitida = models.IntegerField('Lotação Permitida')

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        return self.nome

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class Atleta (models.Model):
    # Atleta é ...
    #
    # UC01 - Manter Atletas
    #     FA01 - Incluir Atleta
    #         2. O sistema apresenta os campos para entrada dos dados:
    #             - Nome (Obrigatório)
    #             - Foto
    #             - CPF (Obrigatório / Não se repete)
    #             - RG (Obrigatório / Não se repete)
    #             - Matrícula (Obrigatório / Não se repete)
    #             - Gênero (Obrigatório)
    #             - Masculino;
    #             - Feminino.
    #             - Data de Nascimento
    #             - Tipo Sanguíneo
    #             - Plano de Saúde
    #             - Nº Carteira SUS
    #             - Medicamento Controlado
    #             - Alergia

    nome = models.CharField(max_length=100)
    foto = StdImageField(upload_to='atletas', variations={'thumb': (124, 124)}, blank=True)  # TODO Aperfeiçoar parâmetros: https://pypi.org/project/django-stdimage/
    cpf = models.CharField('CPF', max_length=11, unique=True)
    rg = models.CharField('RG', max_length=50, unique=True)
    matricula = models.CharField('Matrícula', max_length=20, unique=True)
    genero = models.CharField('Gênero', max_length=1, choices=[['M', 'Masculino'], ['F', 'Femenino']])
    data_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)
    tipo_sanguineo = models.CharField('Tipo Sanguíneo', max_length=3, blank=True)
    plano_saude = models.CharField('Plano de Saúde', max_length=200, blank=True)
    numero_carteira_sus = models.CharField('Nº Carteira do SUS', max_length=20, blank=True)
    medicamento_controlado = models.TextField('Medicamento Controlado', blank=True)
    alergia = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'

    def __str__(self):
        return self.nome

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural
