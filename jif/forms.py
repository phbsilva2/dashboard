from django import forms

from .models import (
    UnidadeOrganizacional,
    Modalidade,
    TipoModalidade,
)


class RelatorioAtletasCampusForm(forms.Form):
    unidade_organizacional = forms.ModelChoiceField(UnidadeOrganizacional.objects.all().order_by('nome'), required=False)


class RelatorioAtletasModalidadeForm(forms.Form):
    modalidade = forms.ModelChoiceField(Modalidade.objects.all().order_by('nome'), required=False)


class RelatorioAtletasTipoModalidadeForm(forms.Form):
    tipo_modalidade = forms.ModelChoiceField(TipoModalidade.objects.all().order_by('titulo'), required=False)


class RelatorioInscricoesForm(forms.Form):
    unidade_organizacional = forms.ModelChoiceField(UnidadeOrganizacional.objects.all().order_by('nome'))
    modalidade = forms.ModelChoiceField(Modalidade.objects.all().order_by('nome'))
