from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import UnidadeOrganizacional


class UnidadeOrganizacionalView(View):

    def get(self, request, *args, **kwargs):
        unidadades_organizacionais = UnidadeOrganizacional.objects.all().order_by('nome')
        unidade_organizacional = UnidadeOrganizacional
        context = {
            'unidadades_organizacionais': unidadades_organizacionais,
            'unidade_organizacional': unidade_organizacional
        }
        return render(request, 'jif/unidade_organizacional/list.html', context)


class UnidadeOrganizacionalDetailView(PermissionRequiredMixin, DetailView):
    model = UnidadeOrganizacional
    permission_required = 'jif.view_unidadeorganizacional'
    template_name = 'jif/unidade_organizacional/detail.html'
    context_object_name = 'unidade_organizacional'


class UnidadeOrganizacionalCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = UnidadeOrganizacional
    fields = ["nome"]
    permission_required = 'jif.add_unidadeorganizacional'
    template_name = 'jif/unidade_organizacional/form.html'
    success_message = "'%(nome)s' foi adicionado com sucesso!"
    success_url = "/unidadeorganizacional_create"


class UnidadeOrganizacionalUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UnidadeOrganizacional
    fields = ["nome"]
    permission_required = 'jif.change_unidadeorganizacional'
    template_name = 'jif/unidade_organizacional/form.html'
    context_object_name = 'unidade_organizacional'
    success_message = "'%(nome)s' foi alterado com sucesso!"
    success_url = "/unidadeorganizacional"


class UnidadeOrganizacionalDeleteView(PermissionRequiredMixin, DeleteView):
    model = UnidadeOrganizacional
    permission_required = 'jif.delete_unidadeorganizacional'
    template_name = 'jif/unidade_organizacional/confirm_delete.html'
    context_object_name = 'unidade_organizacional'
    success_url = "/unidadeorganizacional"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"'{self.get_object()}' foi excluído com sucesso!")
        return super(UnidadeOrganizacionalDeleteView, self).delete(request, *args, **kwargs)
