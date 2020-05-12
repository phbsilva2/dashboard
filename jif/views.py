from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import (
    UnidadeOrganizacional,
)


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'jif/index.html'


from django.shortcuts import render
from django.core.paginator import Paginator


def unidadeOrganizacionalList(request):
    search = request.GET.get('search')
    unidadades_organizacionais = None

    if search:
        unidadades_organizacionais_list = UnidadeOrganizacional.objects.filter(nome__icontains=search).order_by('nome')
    else:
        unidadades_organizacionais_list = UnidadeOrganizacional.objects.all().order_by('nome')

    if unidadades_organizacionais_list:

        paginator = Paginator(unidadades_organizacionais_list, 10)

        page = request.GET.get('page')
        unidadades_organizacionais = paginator.get_page(page)

    else:
        messages.info(request, 'Nenhuma Unidade Organizacional localizada!')

    return render(request, 'jif/unidadeorganizacional_list.html',
                  {'unidadades_organizacionais': unidadades_organizacionais})


class UnidadeOrganizacionalDetailView(PermissionRequiredMixin, DetailView):
    model = UnidadeOrganizacional
    permission_required = 'core.view_unidadeorganizacional'
    template_name = 'jif/unidadeorganizacional_detail.html'
    context_object_name = 'unidade_organizacional'


class UnidadeOrganizacionalCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = UnidadeOrganizacional
    fields = ["nome"]
    permission_required = 'core.add_unidadeorganizacional'
    template_name = 'jif/unidadeorganizacional_form.html'
    success_message = "Unidade Organizacional adicionada com sucesso!"
    success_url = "/unidadeorganizacional"


class UnidadeOrganizacionalUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UnidadeOrganizacional
    fields = ["nome"]
    permission_required = 'core.change_unidadeorganizacional'
    template_name = 'jif/unidadeorganizacional_form.html'
    context_object_name = 'unidade_organizacional'
    success_message = "Unidade Organizacional alterada com sucesso!"
    success_url = "/unidadeorganizacional"


class UnidadeOrganizacionalDeleteView(PermissionRequiredMixin, DeleteView):
    model = UnidadeOrganizacional
    permission_required = 'core.delete_unidadeorganizacional'
    template_name = 'jif/unidadeorganizacional_confirm_delete.html'
    context_object_name = 'unidade_organizacional'
    success_url = "/unidadeorganizacional"

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"Unidade Organizacional {self.get_object()} excluída com sucesso!")
        return super(UnidadeOrganizacionalDeleteView, self).delete(request, *args, **kwargs)
