from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class UsuarioView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'jif/usuario/detail.html'
