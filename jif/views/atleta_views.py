from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import Atleta


class AtletaView(View):

    def get(self, request, *args, **kwargs):
        atleta = Atleta
        atletas = atleta.objects.all().order_by('nome')
        context = {
            'atleta': atleta,
            'atletas': atletas,
        }
        return render(request, 'jif/atleta/list.html', context)


class AtletaDetailView(PermissionRequiredMixin, DetailView):
    model = Atleta
    permission_required = 'jif.view_atleta'
    template_name = 'jif/atleta/detail.html'
    context_object_name = 'atleta'


class AtletaCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Atleta
    fields = ["campus", "nome", "foto", "cpf", "rg", "matricula", "genero", "data_nascimento",
              "tipo_sanguineo", "plano_saude", "numero_carteira_sus", "medicamento_controlado",
              "alergia"]
    permission_required = 'jif.add_atleta'
    template_name = 'jif/atleta/form.html'
    success_message = "'%(nome)s' foi adicionado com sucesso!"
    success_url = "/atleta_create"


class AtletaUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Atleta
    fields = ["campus", "nome", "foto", "cpf", "rg", "matricula", "genero", "data_nascimento",
              "tipo_sanguineo", "plano_saude", "numero_carteira_sus", "medicamento_controlado",
              "alergia"]
    permission_required = 'jif.change_atleta'
    template_name = 'jif/atleta/form.html'
    context_object_name = 'atleta'
    success_message = "'%(nome)s' foi alterado com sucesso!"
    success_url = "/atleta"


class AtletaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Atleta
    permission_required = 'jif.delete_atleta'
    template_name = 'jif/atleta/confirm_delete.html'
    context_object_name = 'atleta'
    success_url = "/atleta"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"'{self.get_object()}' foi excluído com sucesso!")
        return super(AtletaDeleteView, self).delete(request, *args, **kwargs)
