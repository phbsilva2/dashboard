from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import Prova


class ProvaView(View):

    def get(self, request, *args, **kwargs):
        provas = Prova.objects.all().order_by('nome')
        prova = Prova
        context = {
            'provas': provas,
            'prova': prova
        }
        return render(request, 'jif/prova/list.html', context)


class ProvaDetailView(PermissionRequiredMixin, DetailView):
    model = Prova
    permission_required = 'jif.view_prova'
    template_name = 'jif/prova/detail.html'
    context_object_name = 'prova'


class ProvaCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Prova
    fields = ["nome"]
    permission_required = 'jif.add_prova'
    template_name = 'jif/prova/form.html'
    success_message = "'%(nome)s' foi adicionado com sucesso!"
    success_url = "/prova_create"


class ProvaUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Prova
    fields = ["nome"]
    permission_required = 'jif.change_prova'
    template_name = 'jif/prova/form.html'
    context_object_name = 'prova'
    success_message = "'%(nome)s' foi alterado com sucesso!"
    success_url = "/prova"


class ProvaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Prova
    permission_required = 'jif.delete_prova'
    template_name = 'jif/prova/confirm_delete.html'
    context_object_name = 'prova'
    success_url = "/prova"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"'{self.get_object()}' foi excluído com sucesso!")
        return super(ProvaDeleteView, self).delete(request, *args, **kwargs)
