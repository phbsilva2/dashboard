from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import TipoModalidade


class TipoModalidadeView(View):

    def get(self, request, *args, **kwargs):
        tipos_modalidade = TipoModalidade.objects.all().order_by('titulo')
        tipo_modalidade = TipoModalidade
        context = {
            'tipos_modalidade': tipos_modalidade,
            'tipo_modalidade': tipo_modalidade
        }
        return render(request, 'jif/tipo_modalidade/list.html', context)


class TipoModalidadeDetailView(PermissionRequiredMixin, DetailView):
    model = TipoModalidade
    permission_required = 'jif.view_tipomodalidade'
    template_name = 'jif/tipo_modalidade/detail.html'
    context_object_name = 'tipo_modalidade'


class TipoModalidadeCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = TipoModalidade
    fields = ["titulo"]
    permission_required = 'jif.add_tipomodalidade'
    template_name = 'jif/tipo_modalidade/form.html'
    success_message = "'%(titulo)s' foi adicionado com sucesso!"
    success_url = "/tipomodalidade_create"


class TipoModalidadeUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TipoModalidade
    fields = ["titulo"]
    permission_required = 'jif.change_tipomodalidade'
    template_name = 'jif/tipo_modalidade/form.html'
    context_object_name = 'tipo_modalidade'
    success_message = "'%(titulo)s' foi alterado com sucesso!"
    success_url = "/tipomodalidade"


class TipoModalidadeDeleteView(PermissionRequiredMixin, DeleteView):
    model = TipoModalidade
    permission_required = 'jif.delete_tipomodalidade'
    template_name = 'jif/tipo_modalidade/confirm_delete.html'
    context_object_name = 'tipo_modalidade'
    success_url = "/tipomodalidade"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"'{self.get_object()}' foi excluído com sucesso!")
        return super(TipoModalidadeDeleteView, self).delete(request, *args, **kwargs)
