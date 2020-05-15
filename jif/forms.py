from django import forms

from .models import (
    UnidadeOrganizacional,
    Modalidade,
)


class RelatorioAtletasCampusForm(forms.Form):
    unidade_organizacional = forms.ModelChoiceField(UnidadeOrganizacional.objects.all().order_by('nome'), required=False)


class RelatorioAtletasModalidadeForm(forms.Form):
    modalidade = forms.ModelChoiceField(Modalidade.objects.all().order_by('nome'), required=False)
