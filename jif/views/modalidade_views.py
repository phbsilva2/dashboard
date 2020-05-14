from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import Modalidade


class ModalidadeView(View):

    def get(self, request, *args, **kwargs):
        modalidade = Modalidade
        modalidades = modalidade.objects.all().order_by('nome')
        context = {
            'modalidade': modalidade,
            'modalidades': modalidades,
        }
        return render(request, 'jif/modalidade/list.html', context)


class ModalidadeDetailView(PermissionRequiredMixin, DetailView):
    model = Modalidade
    permission_required = 'jif.view_modalidade'
    template_name = 'jif/modalidade/detail.html'
    context_object_name = 'modalidade'


class ModalidadeCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Modalidade
    fields = ["nome", "sigla", "tipo", "tipo_modalidade"]
    permission_required = 'jif.add_modalidade'
    template_name = 'jif/modalidade/form.html'
    success_message = "'%(nome)s' foi adicionado com sucesso!"
    success_url = "/modalidade_create"


class ModalidadeUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Modalidade
    fields = ["nome", "sigla", "tipo", "tipo_modalidade"]
    permission_required = 'jif.change_modalidade'
    template_name = 'jif/modalidade/form.html'
    context_object_name = 'modalidade'
    success_message = "'%(nome)s' foi alterado com sucesso!"
    success_url = "/modalidade"


class ModalidadeDeleteView(PermissionRequiredMixin, DeleteView):
    model = Modalidade
    permission_required = 'jif.delete_modalidade'
    template_name = 'jif/modalidade/confirm_delete.html'
    context_object_name = 'modalidade'
    success_url = "/modalidade"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"'{self.get_object()}' foi excluído com sucesso!")
        return super(ModalidadeDeleteView, self).delete(request, *args, **kwargs)
