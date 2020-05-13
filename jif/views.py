from django.views.generic import View, TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from .models import (
    UnidadeOrganizacional,
)


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'jif/index.html'


class UnidadeOrganizacionalView(View):

    def get(self, request, *args, **kwargs):
        unidadades_organizacionais = UnidadeOrganizacional.objects.all().order_by('nome')
        context = {
            'unidadades_organizacionais': unidadades_organizacionais
        }
        return render(request, 'jif/unidadeorganizacional_list.html', context)


class UnidadeOrganizacionalDetailView(PermissionRequiredMixin, DetailView):
    model = UnidadeOrganizacional
    permission_required = 'core.view_unidadeorganizacional'
    template_name = 'jif/unidadeorganizacional_detail.html'
    context_object_name = 'unidade_organizacional'


class UnidadeOrganizacionalCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = UnidadeOrganizacional
    fields = ["nome"]
    permission_required = 'core.add_unidadeorganizacional'
    template_name = 'jif/unidadeorganizacional_form.html'
    success_message = "Unidade Organizacional adicionada com sucesso!"
    success_url = "/unidadeorganizacional"


class UnidadeOrganizacionalUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UnidadeOrganizacional
    fields = ["nome"]
    permission_required = 'core.change_unidadeorganizacional'
    template_name = 'jif/unidadeorganizacional_form.html'
    context_object_name = 'unidade_organizacional'
    success_message = "Unidade Organizacional alterada com sucesso!"
    success_url = "/unidadeorganizacional"


class UnidadeOrganizacionalDeleteView(PermissionRequiredMixin, DeleteView):
    model = UnidadeOrganizacional
    permission_required = 'core.delete_unidadeorganizacional'
    template_name = 'jif/unidadeorganizacional_confirm_delete.html'
    context_object_name = 'unidade_organizacional'
    success_url = "/unidadeorganizacional"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"Unidade Organizacional {self.get_object()} excluída com sucesso!")
        return super(UnidadeOrganizacionalDeleteView, self).delete(request, *args, **kwargs)
