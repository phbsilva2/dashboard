from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from jif.models import (
    Inscricao,
)

from jif.forms import (
    RelatorioAtletasCampusForm,
    RelatorioAtletasModalidadeForm,
    RelatorioAtletasTipoModalidadeForm,
    RelatorioInscricoesForm,
)

from jif.reports import inscricao_pdf


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
def fichaisncricao(request, uo_id, modalidade_id):
    dados_inscritos = []
    uo_nome = ""
    modalidade_nome = ""

    inscricoes = Inscricao.objects.filter(unidade_organizacional__pk=uo_id, modalidade__pk=modalidade_id)
    if inscricoes:
        for inscr in inscricoes:
            dados_inscrito = []
            dados_inscrito.append(str(inscr.atleta.nome))
            if inscr.atleta.data_nascimento:
                dados_inscrito.append('{:%d/%m/%Y}'.format(inscr.atleta.data_nascimento))
            else:
                dados_inscrito.append(None)
            dados_inscrito.append(str(inscr.atleta.rg))
            dados_inscrito.append(str(inscr.atleta.matricula))
            if not uo_nome:
                uo_nome = inscr.unidade_organizacional.nome
            if not modalidade_nome:
                modalidade_nome = inscr.modalidade.nome

            dados_inscritos.append(dados_inscrito)

        return inscricao_pdf(uo_nome, modalidade_nome, dados_inscritos)
