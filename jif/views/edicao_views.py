from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from jif.models import (
    Edicao,
    Etapa,
    EdicaoCategoria,
    EdicaoModalidade,
    EdicaoModalidadeProva,
    Prova
)


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
    fields = ["nome", "data_inicio_edicao", "data_termino_edicao", "ativo"]
    permission_required = 'jif.change_edicao'
    template_name = 'jif/edicao/form.html'
    context_object_name = 'edicao'
    success_message = "'%(nome)s' foi alterado com sucesso!"
    success_url = "/edicao"

    def get_context_data(self, **kwargs):
        edicao = self.get_object()
        context = super(EdicaoUpdateView, self).get_context_data(**kwargs)
        context['etapas_edicao'] = Etapa.objects.filter(edicao_id=edicao.id) \
            .order_by('nome')
        context['categorias_edicao'] = EdicaoCategoria.objects.filter(edicao_id=edicao.id)\
            .order_by('categoria__nome')
        context['modalidades_edicao'] = EdicaoModalidade.objects.filter(edicao_id=edicao.id)\
            .order_by('modalidade__nome')
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


class EdicaoEtapaCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Etapa
    fields = ["nome", "data_inicio_etapa", "data_termino_etapa", "data_inicio_inscricao",
              "data_termino_inscricao", "campi"]
    permission_required = 'jif.add_etapa'
    template_name = 'jif/edicao/etapa/form.html'
    success_message = "A etapa '%(etapa)s' foi adicionada com sucesso!"

    def get_context_data(self, **kwargs):
        edicao_id = self.kwargs['pk']
        context = super(EdicaoEtapaCreateView, self).get_context_data(**kwargs)
        context['edicao_id'] = edicao_id
        return context

    def form_valid(self, form):
        edicao_id = self.kwargs['pk']
        obj = form.save(commit=False)
        obj.edicao = Edicao.objects.get(pk=edicao_id)
        try:
            obj.save()
            return HttpResponseRedirect(f'/edicao/{edicao_id}/update')
            # return super(EdicaoCategoriaCreateView, self).form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'Essa Etapa já foi cadastrada na Edição.')
            return self.render_to_response(self.get_context_data(form=form))
        except Exception as e:
            messages.error(self.request, e)
            return self.render_to_response(self.get_context_data(form=form))


class EdicaoEtapaUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Etapa
    fields = ["nome", "data_inicio_etapa", "data_termino_etapa", "data_inicio_inscricao",
              "data_termino_inscricao", "campi", "ativo"]
    permission_required = 'jif.change_etapa'
    template_name = 'jif/edicao/etapa/form.html'
    context_object_name = 'etapa'
    success_message = "A etapa '%(nome)s' foi alterada com sucesso!"

    def get_success_url(self, **kwargs):
        edicao_id = self.object.edicao.id
        return f'/edicao/{edicao_id}/update'

    def get_context_data(self, **kwargs):
        edicao_id = self.object.edicao.id
        context = super(EdicaoEtapaUpdateView, self).get_context_data(**kwargs)
        context['edicao_id'] = edicao_id
        return context


class EdicaoEtapaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Etapa
    permission_required = 'jif.delete_etapa'
    template_name = 'jif/edicao/etapa/confirm_delete.html'
    context_object_name = 'etapa'

    def get_success_url(self, **kwargs):
        edicao_id = self.object.edicao.id
        return f'/edicao/{edicao_id}/update'

    def get_context_data(self, **kwargs):
        edicao_id = self.object.edicao.id
        context = super(EdicaoEtapaDeleteView, self).get_context_data(**kwargs)
        context['edicao_id'] = edicao_id
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"A etapa '{self.get_object()}' foi excluída com sucesso!")
        return super(EdicaoEtapaDeleteView, self).delete(request, *args, **kwargs)


class EdicaoCategoriaCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = EdicaoCategoria
    fields = ["categoria", "regras"]
    permission_required = 'jif.add_edicao'
    template_name = 'jif/edicao/categoria/form.html'
    success_message = "A categoria '%(categoria)s' foi adicionada com sucesso!"

    def get_context_data(self, **kwargs):
        edicao_id = self.kwargs['pk']
        context = super(EdicaoCategoriaCreateView, self).get_context_data(**kwargs)
        context['edicao_id'] = edicao_id
        return context

    def form_valid(self, form):
        edicao_id = self.kwargs['pk']
        obj = form.save(commit=False)
        obj.edicao = Edicao.objects.get(pk=edicao_id)
        try:
            obj.save()
            return HttpResponseRedirect(f'/edicao/{edicao_id}/update')
            # return super(EdicaoCategoriaCreateView, self).form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'Essa Categoria já foi cadastrada na Edição.')
            return self.render_to_response(self.get_context_data(form=form))
        except Exception as e:
            messages.error(self.request, e)
            return self.render_to_response(self.get_context_data(form=form))


class EdicaoCategoriaUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = EdicaoCategoria
    fields = ["categoria", "regras", "ativo"]
    permission_required = 'jif.change_edicao'
    template_name = 'jif/edicao/categoria/form.html'
    context_object_name = 'edicaocategoria'
    success_message = "A categoria '%(categoria)s' foi alterada com sucesso!"

    def get_success_url(self, **kwargs):
        edicao_id = self.object.edicao.id
        return f'/edicao/{edicao_id}/update'

    def get_context_data(self, **kwargs):
        edicao_id = self.object.edicao.id
        context = super(EdicaoCategoriaUpdateView, self).get_context_data(**kwargs)
        context['edicao_id'] = edicao_id
        return context


class EdicaoCategoriaDeleteView(PermissionRequiredMixin, DeleteView):
    model = EdicaoCategoria
    permission_required = 'jif.delete_edicao'
    template_name = 'jif/edicao/categoria/confirm_delete.html'
    context_object_name = 'edicao_categoria'

    def get_success_url(self, **kwargs):
        edicao_id = self.object.edicao.id
        return f'/edicao/{edicao_id}/update'

    def get_context_data(self, **kwargs):
        edicao_id = self.object.edicao.id
        context = super(EdicaoCategoriaDeleteView, self).get_context_data(**kwargs)
        context['edicao_id'] = edicao_id
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"A categoria '{self.get_object()}' foi excluída com sucesso!")
        return super(EdicaoCategoriaDeleteView, self).delete(request, *args, **kwargs)


class EdicaoModalidadeCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = EdicaoModalidade
    fields = ["modalidade", "genero", "limite_participantes_modalidade", "ativo"]
    permission_required = 'jif.add_edicao'
    template_name = 'jif/edicao/modalidade/form.html'
    success_message = "A modalidade '%(modalidade)s' foi adicionada com sucesso!"

    def get_context_data(self, **kwargs):
        edicao_id = self.kwargs['pk']
        context = super(EdicaoModalidadeCreateView, self).get_context_data(**kwargs)
        context['edicao_id'] = edicao_id
        return context

    def form_valid(self, form):
        edicao_id = self.kwargs['pk']
        obj = form.save(commit=False)
        obj.edicao = Edicao.objects.get(pk=edicao_id)
        try:
            obj.save()
            return HttpResponseRedirect(f'/edicao/{edicao_id}/update')
            # return super(EdicaoModalidadeCreateView, self).form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'Essa Modalidade já foi cadastrada na Edição.')
            return self.render_to_response(self.get_context_data(form=form))
        except Exception as e:
            messages.error(self.request, e)
            return self.render_to_response(self.get_context_data(form=form))


class EdicaoModalidadeUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = EdicaoModalidade
    fields = ["modalidade", "genero", "limite_participantes_modalidade", "ativo"]
    permission_required = 'jif.change_edicao'
    template_name = 'jif/edicao/modalidade/form.html'
    context_object_name = 'edicaomodalidade'
    success_message = "A modalidade '%(modalidade)s' foi alterada com sucesso!"

    def get_success_url(self, **kwargs):
        edicao_id = self.object.edicao.id
        return f'/edicao/{edicao_id}/update'

    def get_context_data(self, **kwargs):
        edicao_modalidade_id = self.object.id
        context = super(EdicaoModalidadeUpdateView, self).get_context_data(**kwargs)
        context['edicao_modalidade_id'] = edicao_modalidade_id
        context['provas_edicao'] = EdicaoModalidadeProva\
            .objects.filter(edicao_modalidade__id=edicao_modalidade_id) \
            .order_by('edicao_modalidade__modalidade__nome', 'prova__nome')
        return context


class EdicaoModalidadeDeleteView(PermissionRequiredMixin, DeleteView):
    model = EdicaoModalidade
    permission_required = 'jif.delete_edicao'
    template_name = 'jif/edicao/modalidade/confirm_delete.html'
    context_object_name = 'edicao_modalidade'

    def get_success_url(self, **kwargs):
        edicao_id = self.object.edicao.id
        return f'/edicao/{edicao_id}/update'

    def get_context_data(self, **kwargs):
        edicao_id = self.object.edicao.id
        context = super(EdicaoModalidadeDeleteView, self).get_context_data(**kwargs)
        context['edicao_id'] = edicao_id
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"A modalidade '{self.get_object()}' foi excluída com sucesso!")
        return super(EdicaoModalidadeDeleteView, self).delete(request, *args, **kwargs)


class EdicaoModalidadeProvaCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = EdicaoModalidadeProva
    fields = ["prova", "limite_equipe_campus", "limite_participante_equipe",
              "limite_participante_individual", "ativo"]
    permission_required = 'jif.add_edicao'
    template_name = 'jif/edicao/prova/form.html'
    success_message = "A prova '%(prova)s' foi adicionada com sucesso!"

    def get_context_data(self, **kwargs):
        edicao_id = self.kwargs['pk']
        context = super(EdicaoModalidadeProvaCreateView, self).get_context_data(**kwargs)
        context['edicao_id'] = edicao_id
        return context

    def get_form(self, *args, **kwargs):
        edicao_modalidade_id = self.kwargs['pk']
        edicao_modalidade = EdicaoModalidade.objects.get(pk=edicao_modalidade_id)
        form = super(EdicaoModalidadeProvaCreateView, self).get_form(*args, **kwargs)
        form.fields['prova'].queryset = Prova.objects.filter(modalidade_id=edicao_modalidade.modalidade)
        return form

    def form_valid(self, form):
        edicao_modalidade_id = self.kwargs['pk']
        obj = form.save(commit=False)
        obj.edicao_modalidade = EdicaoModalidade.objects.get(pk=edicao_modalidade_id)
        try:
            obj.save()
            return HttpResponseRedirect(f'/edicao/modalidade/{edicao_modalidade_id}/update')
            # return super(EdicaoModalidadeCreateView, self).form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'Essa Prova já foi cadastrada na Edição.')
            return self.render_to_response(self.get_context_data(form=form))
        except Exception as e:
            messages.error(self.request, e)
            return self.render_to_response(self.get_context_data(form=form))


class EdicaoModalidadeProvaUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = EdicaoModalidadeProva
    fields = ["prova", "limite_equipe_campus", "limite_participante_equipe",
              "limite_participante_individual", "ativo"]
    permission_required = 'jif.change_edicao'
    template_name = 'jif/edicao/prova/form.html'
    context_object_name = 'edicao_modalidade_prova'
    success_message = "A prova '%(prova)s' foi alterada com sucesso!"

    def get_success_url(self, **kwargs):
        edicao_modalidade_id = self.object.edicao_modalidade.id
        return f'/edicao/modalidade/{edicao_modalidade_id}/update'

    def get_context_data(self, **kwargs):
        edicao_modalidade_id = self.object.edicao_modalidade.id
        context = super(EdicaoModalidadeProvaUpdateView, self).get_context_data(**kwargs)
        context['edicao_modalidade_id'] = edicao_modalidade_id
        context['provas_edicao'] = EdicaoModalidadeProva.objects\
            .filter(edicao_modalidade__id=edicao_modalidade_id) \
            .order_by('edicao_modalidade__modalidade__nome', 'prova__nome')
        return context


class EdicaoModalidadeProvaDeleteView(PermissionRequiredMixin, DeleteView):
    model = EdicaoModalidadeProva
    permission_required = 'jif.delete_edicao'
    template_name = 'jif/edicao/prova/confirm_delete.html'
    context_object_name = 'edicao_modalidade_prova'

    def get_success_url(self, **kwargs):
        edicao_modalidade_id = self.object.edicao_modalidade.id
        return f'/edicao/modalidade/{edicao_modalidade_id}/update'

    def get_context_data(self, **kwargs):
        edicao_modalidade_id = self.object.edicao_modalidade.id
        context = super(EdicaoModalidadeProvaDeleteView, self).get_context_data(**kwargs)
        context['edicao_modalidade_id'] = edicao_modalidade_id
        context['provas_edicao'] = EdicaoModalidadeProva.objects \
            .filter(edicao_modalidade__id=edicao_modalidade_id) \
            .order_by('edicao_modalidade__modalidade__nome', 'prova__nome')
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(request, f"A prova '{self.get_object()}' foi excluída com sucesso!")
        return super(EdicaoModalidadeProvaDeleteView, self).delete(request, *args, **kwargs)
