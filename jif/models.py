from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    data_hora_cadastro = models.DateTimeField('Data do Cadastro', auto_now_add=True)
    data_hora_ultima_alteracao = models.DateTimeField('Data da Última Alteração', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Instituto(Base):
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Instituto'
        verbose_name_plural = 'Institutos'

    def __str__(self):
        return self.nome

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class Campus(Base):
    nome = models.CharField(max_length=100)
    instituto = models.ForeignKey(Instituto, on_delete=models.CASCADE, verbose_name='Instituto')

    class Meta:
        unique_together = ['nome', 'instituto']
        verbose_name = 'Campus'
        verbose_name_plural = 'Campi'

    def __str__(self):
        return f"{self.nome} ({self.instituto.sigla})"

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class Edicao(Base):
    nome = models.CharField(max_length=100, unique=True)
    data_inicio_edicao = models.DateField('Data do Início da Edição', blank=False, null=False)
    data_termino_edicao = models.DateField('Data do Término da Edição', blank=False, null=False)

    class Meta:
        verbose_name = 'Edição'
        verbose_name_plural = 'Edições'

    def __str__(self):
        return self.nome

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class Etapa(Base):
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, verbose_name='Edição')
    nome = models.CharField(max_length=100, unique=True)
    data_inicio_etapa = models.DateField('Data do Início da Etapa', blank=False, null=False)
    data_termino_etapa = models.DateField('Data do Término da Etapa', blank=False, null=False)
    data_inicio_inscricao = models.DateField('Data do Início das Inscrições', blank=False, null=False)
    data_termino_inscricao = models.DateField('Data do Término das Inscrições', blank=False, null=False)
    campi = models.ManyToManyField(Campus)

    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'

    def __str__(self):
        return self.nome

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class EdicaoCampus(models.Model):
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, verbose_name='Edição')
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, verbose_name='Campus')

    class Meta:
        verbose_name = 'Campus da Edição'
        verbose_name_plural = 'Campi da Edição'

    def __str__(self):
        return f"{self.pk}"

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class Categoria(Base):
    nome = models.CharField(max_length=100, unique=True)
    idade_minima = models.IntegerField('Idade Mínima', blank=True, null=True)
    idade_maxima = models.IntegerField('Idade Máxima', blank=True, null=True)

    class Meta:
        verbose_name = 'Categoria Etária'
        verbose_name_plural = 'Categorias Etárias'

    def __str__(self):
        return self.nome

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class EdicaoCategoria(Base):
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, verbose_name='Edição')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    regras = models.TextField('Regras', blank=True)

    class Meta:
        unique_together = ['edicao', 'categoria']
        verbose_name = 'Categoria da Edição'
        verbose_name_plural = 'Categorias da Edição'

    def __str__(self):
        return f"{self.edicao} {self.categoria}"

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class Modalidade(Base):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=[['I', 'Individual'], ['C', 'Coletivo']])

    class Meta:
        unique_together = ['nome', 'tipo']
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        return f"{self.nome} {'Individual' if self.tipo == 'I' else 'Coletivo'}"

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class EdicaoModalidade(Base):
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, verbose_name='Edição')
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, verbose_name='Modalidade')
    genero = models.CharField('Gênero', max_length=1, choices=[['M', 'Masculino'], ['F', 'Femenino']])
    limite_participantes_modalidade = models.IntegerField('Limite de Participantes na Modalidade', blank=False, null=False)

    class Meta:
        unique_together = ['edicao', 'modalidade', 'genero']
        verbose_name = 'Modalidade da Edição'
        verbose_name_plural = 'Modalidades da Edição'

    def __str__(self):
        return f"{self.modalidade} {'Masculino' if self.genero == 'M' else 'Femenino'} - {self.edicao}"

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class Prova(Base):
    nome = models.CharField(max_length=100, unique=True)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, verbose_name='Modalidade')

    class Meta:
        verbose_name = 'Prova'
        verbose_name_plural = 'Provas'

    def __str__(self):
        return self.nome

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class EdicaoModalidadeProva(Base):
    edicao_modalidade = models.ForeignKey(EdicaoModalidade, on_delete=models.CASCADE, verbose_name='Modalidade')
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE, verbose_name='Prova')
    limite_equipe_campus = models.IntegerField('Limite de Equipe por Campus', blank=False, null=False)
    limite_participante_equipe = models.IntegerField('Limite de Participante por Equipe', blank=False, null=False)
    limite_participante_individual = models.IntegerField('Limite de Participante Individual', blank=False, null=False)

    class Meta:
        unique_together = ['edicao_modalidade', 'prova']
        verbose_name = 'Prova da Modalidade'
        verbose_name_plural = 'Provas da Modalidade'

    def __str__(self):
        return f"{self.prova} - {self.edicao_modalidade}"

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class Atleta(Base):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, verbose_name='Campus')
    nome = models.CharField(max_length=100)
    foto = StdImageField(upload_to='atletas', variations={'thumb': (124, 124)},
                         blank=True)  # TODO Aperfeiçoar parâmetros: https://pypi.org/project/django-stdimage/
    cpf = models.CharField('CPF', max_length=11, unique=True)
    rg = models.CharField('RG', max_length=50, unique=True)
    matricula = models.CharField('Matrícula', max_length=20, unique=True)
    genero = models.CharField('Gênero', max_length=1, choices=[['M', 'Masculino'], ['F', 'Femenino']])
    data_nascimento = models.DateField('Data de Nascimento', blank=False, null=False)
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


class Inscricao(Base):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE, verbose_name='Atleta')
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, verbose_name='Campus')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, verbose_name='Etapa')
    edicao_prova = models.ForeignKey(EdicaoModalidadeProva, on_delete=models.CASCADE, verbose_name='Prova')

    objects = models.Manager()

    class Meta:
        unique_together = ['atleta', 'etapa', 'edicao_prova']
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    def __str__(self):
        return f"{self.pk}"

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural
