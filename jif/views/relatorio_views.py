from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from jif.models import (
    Inscricao,
)

from jif.forms import (
    RelatorioAtletasCampusForm,
    RelatorioAtletasModalidadeForm,
    RelatorioAtletasProvaForm,
    RelatorioInscricoesForm,
)

from jif.reports import inscricao_pdf


@login_required
def atleta_campus(request):
    form = RelatorioAtletasCampusForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['campus']:
                campus_id = form.cleaned_data['campus'].pk
                inscricoes = Inscricao.objects.filter(campus__pk=campus_id).order_by('atleta__nome')
                mostrar_campus = False
            else:
                inscricoes = Inscricao.objects.all().order_by('campus__nome', 'atleta__nome')
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
                inscricoes = Inscricao.objects\
                    .filter(edicao_prova__edicao_modalidade__modalidade__pk=modalidade_id)\
                    .order_by('atleta__nome')
                mostrar_modalidade = False
            else:
                inscricoes = Inscricao.objects.all()\
                    .order_by('edicao_prova__edicao_modalidade__modalidade__nome', 'atleta__nome')
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
def atleta_prova(request):
    form = RelatorioAtletasProvaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['prova']:
                prova_id = form.cleaned_data['prova'].pk
                inscricoes = Inscricao.objects.filter(edicao_prova__prova__pk=prova_id).order_by('atleta__nome')
                mostrar_prova = False
            else:
                inscricoes = Inscricao.objects.all().order_by('edicao_prova__prova', 'atleta__nome')
                mostrar_prova = True

            return render(request, 'jif/relatorio/atletaprova.html',
                          {'form': form, 'inscricoes': inscricoes, 'mostrar_prova': mostrar_prova})
    else:
        form = RelatorioAtletasProvaForm()
    context = {
        'form': form
    }
    return render(request, 'jif/relatorio/atletaprova.html', context)


@login_required
def inscricoes_atletas(request):
    form = RelatorioInscricoesForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            edicao_id = form.cleaned_data['edicao'].pk
            campus_id = form.cleaned_data['campus'].pk

            inscricoes = Inscricao.objects.filter(edicao_prova__edicao_modalidade__edicao__pk=edicao_id,
                                                  campus__pk=campus_id)\
                .order_by('atleta__nome', 'edicao_prova__prova__nome')

            return render(request, 'jif/relatorio/inscricoesatletas.html',
                          {'form': form,
                           'inscricoes': inscricoes,
                           'edicao': edicao_id,
                           'campus': campus_id})
    else:
        form = RelatorioInscricoesForm()
    context = {
        'form': form
    }
    return render(request, 'jif/relatorio/inscricoesatletas.html', context)


@login_required
def fichaisncricao(request, edicao_id, campus_id):
    dados_inscritos = []
    edicao_nome = ""
    campus_nome = ""
    instituto_nome = ""

    inscricoes = Inscricao.objects.filter(edicao_prova__edicao_modalidade__edicao__pk=edicao_id,
                                          campus__pk=campus_id).order_by('atleta__nome', 'edicao_prova__prova__nome')
    dados_inscrito = []
    if inscricoes:
        atleta = ""
        for inscr in inscricoes:
            if atleta != str(inscr.atleta.nome):
                if atleta != "":
                    dados_inscritos.append(dados_inscrito)

                atleta = str(inscr.atleta.nome)
                dados_inscrito = []
                dados_inscrito.append(str(inscr.atleta.nome))
                if inscr.atleta.data_nascimento:
                    dados_inscrito.append('{:%d/%m/%Y}'.format(inscr.atleta.data_nascimento))
                else:
                    dados_inscrito.append(None)
                dados_inscrito.append(str(inscr.atleta.rg))
                dados_inscrito.append(str(inscr.atleta.matricula))
                dados_inscrito.append(str(inscr.edicao_prova.prova.nome))
            else:
                dados_inscrito[4] = f'{dados_inscrito[4]}\n{inscr.edicao_prova.prova.nome}'

        dados_inscritos.append(dados_inscrito)

        if not campus_nome:
            campus_nome = inscr.campus.nome
            instituto_nome = inscr.campus.instituto
        if not edicao_nome:
            edicao_nome = inscr.edicao_prova.edicao_modalidade.edicao

        return inscricao_pdf(instituto_nome, campus_nome, edicao_nome, dados_inscritos)
