from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from jif.models import Modalidade, Atleta, Inscricao


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'jif/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qtd_modalidades"] = Modalidade.objects.count()
        context["qtd_atletas"] = Atleta.objects.count()
        context["qtd_inscricoes"] = Inscricao.objects.count()

        return context
