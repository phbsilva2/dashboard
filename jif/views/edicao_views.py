from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import Edicao, EdicaoCategoria


class EdicaoView(View):

    def get(self, request, *args, **kwargs):
        edicoes = Edicao.objects.all().order_by('nome')
        edicao = Edicao
        context = {
            'edicoes': edicoes,
            'edicao': edicao
        }
        return render(request, 'jif/edicao/list.html', context)


class EdicaoDetailView(PermissionRequiredMixin, DetailView):
    model = Edicao
    permission_required = 'jif.view_edicao'
    template_name = 'jif/edicao/detail.html'
    context_object_name = 'edicao'


class EdicaoCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Edicao
    fields = ["nome", "data_inicio_edicao", "data_termino_edicao"]
    permission_required = 'jif.add_edicao'
    template_name = 'jif/edicao/form.html'
    success_message = "'%(nome)s' foi adicionado com sucesso!"
    success_url = "/edicao_create"


class EdicaoUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Edicao
    fields = ["nome", "data_inicio_edicao", "data_termino_edicao"]
    permission_required = 'jif.change_edicao'
    template_name = 'jif/edicao/form.html'
    context_object_name = 'edicao'
    success_message = "'%(nome)s' foi alterado com sucesso!"
    success_url = "/edicao"

    def get_context_data(self, **kwargs):
        teste = self.get_object()
        context = super(EdicaoUpdateView, self).get_context_data(**kwargs)
        context['categorias_edicao'] = EdicaoCategoria.objects.filter(edicao_id=teste.id).order_by('id')
        return context


class EdicaoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Edicao
    permission_required = 'jif.delete_edicao'
    template_name = 'jif/edicao/confirm_delete.html'
    context_object_name = 'edicao'
    success_url = "/edicao"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"'{self.get_object()}' foi excluído com sucesso!")
        return super(EdicaoDeleteView, self).delete(request, *args, **kwargs)


class EdicaoCategoriaCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = EdicaoCategoria
    fields = ["categoria", "regras"]
    permission_required = 'jif.add_edicao'
    template_name = 'jif/edicao/categoria/form.html'
    success_message = "'%(categoria)s' foi adicionado com sucesso!"
    success_url = "/edicao_create"

    def form_valid(self, form):
        edicao_id = self.kwargs['pk']
        obj = form.save(commit=False)
        obj.edicao = Edicao.objects.get(pk=edicao_id)
        obj.save()

        messages.success(self.request, 'Categoria foi adicionado com sucesso!')
        return HttpResponseRedirect(reverse('edicao'))
