from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import Campus


class CampusView(View):

    def get(self, request, *args, **kwargs):
        campi = Campus.objects.all().order_by('nome')
        campus = Campus
        context = {
            'campi': campi,
            'campus': campus
        }
        return render(request, 'jif/campus/list.html', context)


class CampusDetailView(PermissionRequiredMixin, DetailView):
    model = Campus
    permission_required = 'jif.view_campus'
    template_name = 'jif/campus/detail.html'
    context_object_name = 'campus'


class CampusCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Campus
    fields = ["nome", "instituto", "ativo"]
    permission_required = 'jif.add_campus'
    template_name = 'jif/campus/form.html'
    success_message = "'%(nome)s' foi adicionado com sucesso!"
    success_url = "/campus_create"


class CampusUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Campus
    fields = ["nome", "instituto", "ativo"]
    permission_required = 'jif.change_campus'
    template_name = 'jif/campus/form.html'
    context_object_name = 'campus'
    success_message = "'%(nome)s' foi alterado com sucesso!"
    success_url = "/campus"


class CampusDeleteView(PermissionRequiredMixin, DeleteView):
    model = Campus
    permission_required = 'jif.delete_campus'
    template_name = 'jif/campus/confirm_delete.html'
    context_object_name = 'campus'
    success_url = "/campus"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"'{self.get_object()}' foi excluído com sucesso!")
        return super(CampusDeleteView, self).delete(request, *args, **kwargs)
