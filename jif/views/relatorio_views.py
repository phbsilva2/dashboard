from django.shortcuts import render

from jif.models import (
    Inscricao,
)

from jif.forms import (
    RelatorioAtletasCampusForm,
)


def atleta_campus(request):
    form = RelatorioAtletasCampusForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['unidade_organizacional']:
                unidade_organizacional_id = form.cleaned_data['unidade_organizacional'].pk
                inscricoes = Inscricao.objects.filter(unidade_organizacional__pk=unidade_organizacional_id).order_by('atleta__nome')
                mostrar_campus = False
            else:
                inscricoes = Inscricao.objects.all().order_by('unidade_organizacional__nome', 'atleta__nome')
                mostrar_campus = True

            return render(request, 'jif/relatorio/atletacampus.html',
                          {'form': form, 'inscricoes': inscricoes, 'mostrar_campus': mostrar_campus})
    else:
        form = RelatorioAtletasCampusForm()
    context = {
        'form': form
    }
    return render(request, 'jif/relatorio/atletacampus.html', context)
