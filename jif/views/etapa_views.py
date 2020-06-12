from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import Etapa


class EtapaView(View):

    def get(self, request, *args, **kwargs):
        etapas = Etapa.objects.all().order_by('nome')
        etapa = Etapa
        context = {
            'etapas': etapas,
            'etapa': etapa
        }
        return render(request, 'jif/etapa/list.html', context)


class EtapaDetailView(PermissionRequiredMixin, DetailView):
    model = Etapa
    permission_required = 'jif.view_etapa'
    template_name = 'jif/etapa/detail.html'
    context_object_name = 'etapa'


class EtapaCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Etapa
    fields = ["nome"]
    permission_required = 'jif.add_etapa'
    template_name = 'jif/etapa/form.html'
    success_message = "'%(nome)s' foi adicionado com sucesso!"
    success_url = "/etapa_create"


class EtapaUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Etapa
    fields = ["nome"]
    permission_required = 'jif.change_etapa'
    template_name = 'jif/etapa/form.html'
    context_object_name = 'etapa'
    success_message = "'%(nome)s' foi alterado com sucesso!"
    success_url = "/etapa"


class EtapaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Etapa
    permission_required = 'jif.delete_etapa'
    template_name = 'jif/etapa/confirm_delete.html'
    context_object_name = 'etapa'
    success_url = "/etapa"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"'{self.get_object()}' foi excluído com sucesso!")
        return super(EtapaDeleteView, self).delete(request, *args, **kwargs)
