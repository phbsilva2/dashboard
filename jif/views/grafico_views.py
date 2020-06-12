from django.views.generic import TemplateView
from django.db.models import Count
from chartjs.views.lines import BaseLineOptionsChartView
from chartjs.colors import COLORS, next_color
from random import shuffle
from jif.models import Inscricao


class GraficoView(TemplateView):
    template_name = 'jif/grafico.html'


class InscricaoCampusMixin(object):

    def get_labels(self):
        labels = ["Inscrições"]
        return labels

    def get_providers(self):
        datasets = []
        inscricoes = Inscricao.objects.all().values('campus__nome').annotate(
            total=Count('campus__nome')).order_by('campus__nome')

        for inscricao in inscricoes:
            datasets.append(inscricao['campus__nome'])
        return datasets

    def get_data(self):
        dados = []
        inscricoes = Inscricao.objects.all().values('campus__nome').annotate(
            total=Count('campus__nome')).order_by('campus__nome')

        for inscricao in inscricoes:
            dados.append([inscricao['total']])
        return dados

    def get_colors(self):
        colors = COLORS[:]
        shuffle(colors)
        return next_color(colors)


    def get_dataset_options(self, index, color):
        default_opt = {
            "backgroundColor": "rgba(%d, %d, %d, 0.5)" % color,
            "borderColor": "rgba(%d, %d, %d, 1)" % color,
            "pointBackgroundColor": "rgba(%d, %d, %d, 1)" % color,
            "pointBorderColor": "#fff",
            "borderWidth": 2,
        }
        return default_opt


class InscricaoCampusJSONView(InscricaoCampusMixin, BaseLineOptionsChartView):
    def get_options(self):
        options = {
            "title": {"display": False, "text": "Título do Gráfico"},
            "elements": {"point": {"pointStyle": "rectRounded", "radius": 10}},
            "responsive": True,
            "scales": {"yAxes": [{"ticks": {"beginAtZero": True, "stepSize": 1}}]}
        }
        return options


class InscricaoModalidadeMixin(object):

    def get_labels(self):
        labels = ["Inscrições"]
        return labels

    def get_providers(self):
        datasets = []
        inscricoes = Inscricao.objects.all().values('modalidade__nome').annotate(
            total=Count('modalidade__nome')).order_by('modalidade__nome')

        for inscricao in inscricoes:
            datasets.append(inscricao['modalidade__nome'])
        return datasets

    def get_data(self):
        dados = []
        inscricoes = Inscricao.objects.all().values('modalidade__nome').annotate(
            total=Count('modalidade__nome')).order_by('modalidade__nome')

        for inscricao in inscricoes:
            dados.append([inscricao['total']])
        return dados

    def get_colors(self):
        colors = COLORS[:]
        shuffle(colors)
        return next_color(colors)

    def get_dataset_options(self, index, color):
        default_opt = {
            "backgroundColor": "rgba(%d, %d, %d, 0.5)" % color,
            "borderColor": "rgba(%d, %d, %d, 1)" % color,
            "pointBackgroundColor": "rgba(%d, %d, %d, 1)" % color,
            "pointBorderColor": "#fff",
            "borderWidth": 2,
        }
        return default_opt


class InscricaoModalidadeJSONView(InscricaoModalidadeMixin, BaseLineOptionsChartView):
    def get_options(self):
        options = {
            "title": {"display": False, "text": "Título do Gráfico"},
            "elements": {"point": {"pointStyle": "rectRounded", "radius": 10}},
            "responsive": True,
            "scales": {"yAxes": [{"ticks": {"beginAtZero": True, "stepSize": 1}}]}
        }
        return options


class InscricaoModalidadeLineMixin(object):

    def get_labels(self):
        labels = []
        inscricoes = Inscricao.objects.all().values('modalidade__nome').annotate(
            total=Count('modalidade__nome')).order_by('total', 'modalidade__nome')

        for inscricao in inscricoes:
            labels.append(inscricao['modalidade__nome'])
        return labels

    def get_providers(self):
        datasets = ["Inscricoes"]

        return datasets

    def get_data(self):
        dados = []
        inscricoes = Inscricao.objects.all().values('modalidade__nome').annotate(
            total=Count('modalidade__nome')).order_by('total', 'modalidade__nome')

        for inscricao in inscricoes:
            dados.append(inscricao['total'])
        return [dados]

    def get_colors(self):
        colors = COLORS[:]
        shuffle(colors)
        return next_color(colors)

    def get_dataset_options(self, index, color):
        default_opt = {
            "backgroundColor": "rgba(%d, %d, %d, 0.5)" % color,
            "borderColor": "rgba(%d, %d, %d, 1)" % color,
            "pointBackgroundColor": "rgba(%d, %d, %d, 1)" % color,
            "pointBorderColor": "#fff",
            "borderWidth": 3,
            "fill": False
        }
        return default_opt


class InscricaoModalidadeLineJSONView(InscricaoModalidadeLineMixin, BaseLineOptionsChartView):
    def get_options(self):
        options = {
            "title": {"display": True, "text": "Inscrições por Modalidade"},
            "elements": {"point": {"pointStyle": "rectRounded", "radius": 10}},
            "responsive": True,
            "scales": {"yAxes": [{"ticks": {"beginAtZero": True, "stepSize": 1}}]},
            "legend": {"display": False}
        }
        return options
