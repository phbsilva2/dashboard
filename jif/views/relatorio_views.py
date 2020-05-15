from django.shortcuts import render

from jif.models import (
    Inscricao,
)

from jif.forms import (
    RelatorioAtletasCampusForm,
    RelatorioAtletasModalidadeForm,
    RelatorioAtletasTipoModalidadeForm,
    RelatorioInscricoesForm,
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


def atleta_modalidade(request):
    form = RelatorioAtletasModalidadeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['modalidade']:
                modalidade_id = form.cleaned_data['modalidade'].pk
                inscricoes = Inscricao.objects.filter(modalidade__pk=modalidade_id).order_by('atleta__nome')
                mostrar_modalidade = False
            else:
                inscricoes = Inscricao.objects.all().order_by('modalidade__nome', 'atleta__nome')
                mostrar_modalidade = True

            return render(request, 'jif/relatorio/atletamodalidade.html',
                          {'form': form, 'inscricoes': inscricoes, 'mostrar_modalidade': mostrar_modalidade})
    else:
        form = RelatorioAtletasModalidadeForm()
    context = {
        'form': form
    }
    return render(request, 'jif/relatorio/atletamodalidade.html', context)


def atleta_tipo_modalidade(request):
    form = RelatorioAtletasTipoModalidadeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['tipo_modalidade']:
                tipo_modalidade_id = form.cleaned_data['tipo_modalidade'].pk
                inscricoes = Inscricao.objects.filter(modalidade__tipo_modalidade__pk=tipo_modalidade_id).order_by('atleta__nome')
                mostrar_tipo_modalidade = False
            else:
                inscricoes = Inscricao.objects.all().order_by('modalidade__tipo_modalidade__titulo', 'atleta__nome')
                mostrar_tipo_modalidade = True

            return render(request, 'jif/relatorio/atletatipomodalidade.html',
                          {'form': form, 'inscricoes': inscricoes, 'mostrar_tipo_modalidade': mostrar_tipo_modalidade})
    else:
        form = RelatorioAtletasTipoModalidadeForm()
    context = {
        'form': form
    }
    return render(request, 'jif/relatorio/atletatipomodalidade.html', context)


def inscricoes_atletas(request):
    form = RelatorioInscricoesForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            unidade_organizacional_id = form.cleaned_data['unidade_organizacional'].pk
            modalidade_id = form.cleaned_data['modalidade'].pk

            inscricoes = Inscricao.objects.filter(unidade_organizacional__pk=unidade_organizacional_id, modalidade__pk=modalidade_id)

            return render(request, 'jif/relatorio/inscricoesatletas.html',
                          {'form': form,
                           'inscricoes': inscricoes,
                           'uo': unidade_organizacional_id,
                           'modalidade': modalidade_id})
    else:
        form = RelatorioInscricoesForm()
    context = {
        'form': form
    }
    return render(request, 'jif/relatorio/inscricoesatletas.html', context)
