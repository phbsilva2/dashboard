from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class GraficoAtletaCampusView(TemplateView):
    template_name = 'jif/grafico.html'


class DadosAtletaCampusView(BaseLineChartView):

    def get_labels(self):
        labels = [
            "Label1"
        ]

        return labels

    def get_providers(self):
        datasets = [
            "DataSet1",
            "DataSet2",
            "DataSet3",
            "DataSet4",
        ]
        return datasets

    def get_data(self):
        dados = [[2], [5], [9], [4]]

        return dados
