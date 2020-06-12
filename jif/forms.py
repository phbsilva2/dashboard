from django import forms

from .models import (
    Instituto,
    Modalidade
)


class RelatorioAtletasCampusForm(forms.Form):
    instituto = forms.ModelChoiceField(Instituto.objects.all().order_by('nome'), required=False)


class RelatorioAtletasModalidadeForm(forms.Form):
    modalidade = forms.ModelChoiceField(Modalidade.objects.all().order_by('nome'), required=False)


class RelatorioAtletasTipoModalidadeForm(forms.Form):
    tipo_modalidade = forms.ModelChoiceField(Instituto.objects.all().order_by('titulo'), required=False)


class RelatorioInscricoesForm(forms.Form):
    instituto = forms.ModelChoiceField(Instituto.objects.all().order_by('nome'))
    modalidade = forms.ModelChoiceField(Modalidade.objects.all().order_by('nome'))
