from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import Categoria


class CategoriaView(View):

    def get(self, request, *args, **kwargs):
        categorias = Categoria.objects.all().order_by('nome')
        categoria = Categoria
        context = {
            'categorias': categorias,
            'categoria': categoria
        }
        return render(request, 'jif/categoria/list.html', context)


class CategoriaDetailView(PermissionRequiredMixin, DetailView):
    model = Categoria
    permission_required = 'jif.view_categoria'
    template_name = 'jif/categoria/detail.html'
    context_object_name = 'categoria'


class CategoriaCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    fields = ["nome"]
    permission_required = 'jif.add_categoria'
    template_name = 'jif/categoria/form.html'
    success_message = "'%(nome)s' foi adicionado com sucesso!"
    success_url = "/categoria_create"


class CategoriaUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    fields = ["nome"]
    permission_required = 'jif.change_categoria'
    template_name = 'jif/categoria/form.html'
    context_object_name = 'categoria'
    success_message = "'%(nome)s' foi alterado com sucesso!"
    success_url = "/categoria"


class CategoriaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Categoria
    permission_required = 'jif.delete_categoria'
    template_name = 'jif/categoria/confirm_delete.html'
    context_object_name = 'categoria'
    success_url = "/categoria"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"'{self.get_object()}' foi excluído com sucesso!")
        return super(CategoriaDeleteView, self).delete(request, *args, **kwargs)
