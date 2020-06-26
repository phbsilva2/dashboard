from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import Instituto


class InstitutoView(View):

    def get(self, request, *args, **kwargs):
        institutos = Instituto.objects.all().order_by('nome')
        instituto = Instituto
        context = {
            'institutos': institutos,
            'instituto': instituto
        }
        return render(request, 'jif/instituto/list.html', context)


class InstitutoDetailView(PermissionRequiredMixin, DetailView):
    model = Instituto
    permission_required = 'jif.view_instituto'
    template_name = 'jif/instituto/detail.html'
    context_object_name = 'instituto'


class InstitutoCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Instituto
    fields = ["nome", "sigla", "ativo"]
    permission_required = 'jif.add_instituto'
    template_name = 'jif/instituto/form.html'
    success_message = "'%(nome)s' foi adicionado com sucesso!"
    success_url = "/instituto_create"


class InstitutoUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Instituto
    fields = ["nome", "sigla", "ativo"]
    permission_required = 'jif.change_instituto'
    template_name = 'jif/instituto/form.html'
    context_object_name = 'instituto'
    success_message = "'%(nome)s' foi alterado com sucesso!"
    success_url = "/instituto"


class InstitutoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Instituto
    permission_required = 'jif.delete_instituto'
    template_name = 'jif/instituto/confirm_delete.html'
    context_object_name = 'instituto'
    success_url = "/instituto"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"'{self.get_object()}' foi excluído com sucesso!")
        return super(InstitutoDeleteView, self).delete(request, *args, **kwargs)
