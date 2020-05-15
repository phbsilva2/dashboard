from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import Inscricao


class InscricaoView(View):

    def get(self, request, *args, **kwargs):
        inscricao = Inscricao
        inscricoes = inscricao.objects.all().order_by('modalidade__nome', 'atleta__nome')
        context = {
            'inscricao': inscricao,
            'inscricoes': inscricoes
        }
        return render(request, 'jif/inscricao/list.html', context)


class InscricaoDetailView(PermissionRequiredMixin, DetailView):
    model = Inscricao
    permission_required = 'jif.view_inscricao'
    template_name = 'jif/inscricao/detail.html'
    context_object_name = 'inscricao'


class InscricaoCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Inscricao
    fields = ["modalidade", "atleta", "unidade_organizacional"]
    permission_required = 'jif.add_inscricao'
    template_name = 'jif/inscricao/form.html'
    success_message = "A inscrição do atleta '%(atleta)s' foi realizada com sucesso!"
    success_url = "/inscricao_create"


class InscricaoUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Inscricao
    fields = ["modalidade", "atleta", "unidade_organizacional"]
    permission_required = 'jif.change_inscricao'
    template_name = 'jif/inscricao/form.html'
    context_object_name = 'inscricao'
    success_message = "A inscrição do atleta '%(atleta)s' foi alterada com sucesso!"
    success_url = "/inscricao"


class InscricaoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Inscricao
    permission_required = 'jif.delete_inscricao'
    template_name = 'jif/inscricao/confirm_delete.html'
    context_object_name = 'inscricao'
    success_url = "/inscricao"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"A inscrição '{self.get_object()}' foi excluída com sucesso!")
        return super(InscricaoDeleteView, self).delete(request, *args, **kwargs)
