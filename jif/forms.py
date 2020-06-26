from django import forms

from .models import (
    Edicao,
    Campus,
    Modalidade,
    Prova
)


class RelatorioAtletasCampusForm(forms.Form):
    campus = forms.ModelChoiceField(Campus.objects.all().order_by('nome'), required=False)


class RelatorioAtletasModalidadeForm(forms.Form):
    modalidade = forms.ModelChoiceField(Modalidade.objects.all().order_by('nome'), required=False)


class RelatorioAtletasProvaForm(forms.Form):
    prova = forms.ModelChoiceField(Prova.objects.all().order_by('nome'), required=False)


class RelatorioInscricoesForm(forms.Form):
    edicao = forms.ModelChoiceField(Edicao.objects.all().order_by('nome'))
    campus = forms.ModelChoiceField(Campus.objects.all().order_by('nome'))
