# Generated by Django 2.2.12 on 2020-05-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jif', '0005_lotacaomodalidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='modalidade',
            name='lotacao_permitida',
            field=models.IntegerField(default=0, verbose_name='Lotação Permitida'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='LotacaoModalidade',
        ),
    ]