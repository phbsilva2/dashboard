# Generated by Django 2.2.13 on 2020-06-23 14:19

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campi',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('idade_minima', models.IntegerField(blank=True, null=True, verbose_name='Idade Mínima')),
                ('idade_maxima', models.IntegerField(blank=True, null=True, verbose_name='Idade Máxima')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Edicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('data_inicio_edicao', models.DateField(verbose_name='Data do Início da Edição')),
                ('data_termino_edicao', models.DateField(verbose_name='Data do Término da Edição')),
            ],
            options={
                'verbose_name': 'Edição',
                'verbose_name_plural': 'Edições',
            },
        ),
        migrations.CreateModel(
            name='EdicaoModalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('genero', models.CharField(choices=[['M', 'Masculino'], ['F', 'Femenino']], max_length=1, verbose_name='Gênero')),
                ('limite_participantes_modalidade', models.IntegerField(verbose_name='Limite de Participantes na Modalidade')),
                ('edicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Edicao', verbose_name='Edição')),
            ],
            options={
                'verbose_name': 'Modalidade da Edição',
                'verbose_name_plural': 'Modalidades da Edição',
            },
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('data_inicio_etapa', models.DateField(verbose_name='Data do Início da Etapa')),
                ('data_termino_etapa', models.DateField(verbose_name='Data do Término da Etapa')),
                ('data_inicio_inscricao', models.DateField(verbose_name='Data do Início das Inscrições')),
                ('data_termino_inscricao', models.DateField(verbose_name='Data do Término das Inscrições')),
                ('campi', models.ManyToManyField(to='jif.Campus')),
                ('edicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Edicao', verbose_name='Edição')),
            ],
            options={
                'verbose_name': 'Etapa',
                'verbose_name_plural': 'Etapas',
            },
        ),
        migrations.CreateModel(
            name='Instituto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('sigla', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Instituto',
                'verbose_name_plural': 'Institutos',
            },
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('tipo', models.CharField(choices=[['I', 'Individual'], ['C', 'Coletivo']], max_length=1)),
            ],
            options={
                'verbose_name': 'Modalidade',
                'verbose_name_plural': 'Modalidades',
            },
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Modalidade', verbose_name='Modalidade')),
            ],
            options={
                'verbose_name': 'Prova',
                'verbose_name_plural': 'Provas',
            },
        ),
        migrations.CreateModel(
            name='EdicaoModalidadeProva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('limite_equipe_campus', models.IntegerField(verbose_name='Limite de Equipe por Campus')),
                ('limite_participante_equipe', models.IntegerField(verbose_name='Limite de Participante por Equipe')),
                ('limite_participante_individual', models.IntegerField(verbose_name='Limite de Participante Individual')),
                ('edicao_modalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.EdicaoModalidade', verbose_name='Modalidade')),
                ('prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Prova', verbose_name='Prova')),
            ],
            options={
                'verbose_name': 'Prova da Modalidade',
                'verbose_name_plural': 'Provas da Modalidade',
                'unique_together': {('edicao_modalidade', 'prova')},
            },
        ),
        migrations.AddField(
            model_name='edicaomodalidade',
            name='modalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Modalidade', verbose_name='Modalidade'),
        ),
        migrations.CreateModel(
            name='EdicaoCampus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Campus', verbose_name='Campus')),
                ('edicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Edicao', verbose_name='Edição')),
            ],
            options={
                'verbose_name': 'Campus da Edição',
                'verbose_name_plural': 'Campi da Edição',
            },
        ),
        migrations.AddField(
            model_name='campus',
            name='instituto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Instituto', verbose_name='Instituto'),
        ),
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100)),
                ('foto', stdimage.models.StdImageField(blank=True, upload_to='atletas')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=50, unique=True, verbose_name='RG')),
                ('matricula', models.CharField(max_length=20, unique=True, verbose_name='Matrícula')),
                ('genero', models.CharField(choices=[['M', 'Masculino'], ['F', 'Femenino']], max_length=1, verbose_name='Gênero')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('tipo_sanguineo', models.CharField(blank=True, max_length=3, verbose_name='Tipo Sanguíneo')),
                ('plano_saude', models.CharField(blank=True, max_length=200, verbose_name='Plano de Saúde')),
                ('numero_carteira_sus', models.CharField(blank=True, max_length=20, verbose_name='Nº Carteira do SUS')),
                ('medicamento_controlado', models.TextField(blank=True, verbose_name='Medicamento Controlado')),
                ('alergia', models.TextField(blank=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Campus', verbose_name='Campus')),
            ],
            options={
                'verbose_name': 'Atleta',
                'verbose_name_plural': 'Atletas',
            },
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Atleta', verbose_name='Atleta')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Campus', verbose_name='Campus')),
                ('edicao_prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.EdicaoModalidadeProva', verbose_name='Prova')),
                ('etapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Etapa', verbose_name='Etapa')),
            ],
            options={
                'verbose_name': 'Inscrição',
                'verbose_name_plural': 'Inscrições',
                'unique_together': {('atleta', 'etapa', 'edicao_prova')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='edicaomodalidade',
            unique_together={('edicao', 'modalidade', 'genero')},
        ),
        migrations.CreateModel(
            name='EdicaoCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cadastro')),
                ('data_hora_ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('regras', models.TextField(blank=True, verbose_name='Regras')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Categoria', verbose_name='Categoria')),
                ('edicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jif.Edicao', verbose_name='Edição')),
            ],
            options={
                'verbose_name': 'Categoria da Edição',
                'verbose_name_plural': 'Categorias da Edição',
                'unique_together': {('edicao', 'categoria')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='campus',
            unique_together={('nome', 'instituto')},
        ),
    ]
