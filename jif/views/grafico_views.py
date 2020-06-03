from django.views.generic import TemplateView
from django.db.models import Count
from chartjs.views.lines import BaseLineChartView
from jif.models import Inscricao


class GraficoInscricaoCampusView(TemplateView):
    template_name = 'jif/grafico.html'


class DadosInscricaoCampusView(BaseLineChartView):

    inscricoes = Inscricao.objects.all().values('unidade_organizacional__nome').annotate(total=Count('unidade_organizacional__nome')).order_by('total')

    def get_labels(self):
        labels = [
            "Inscrições"
        ]

        return labels

    def get_providers(self):
        datasets = []

        for inscricao in self.inscricoes:
            datasets.append(inscricao['unidade_organizacional__nome'])

        return datasets

    def get_data(self):
        dados = []
        for inscricao in self.inscricoes:
            dados.append([inscricao['total']])

        return dados
