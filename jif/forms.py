from django import forms

from .models import (
    UnidadeOrganizacional,
)


class RelatorioAtletasCampusForm(forms.Form):
    unidade_organizacional = forms.ModelChoiceField(UnidadeOrganizacional.objects.all().order_by('nome'), required=False)
