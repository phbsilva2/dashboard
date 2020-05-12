from django.urls import path

from .views import (
    IndexView,
    UnidadeOrganizacionalCreateView,
    UnidadeOrganizacionalDetailView,
    UnidadeOrganizacionalUpdateView,
    UnidadeOrganizacionalDeleteView,
)

from . import views #TODO Retirar

urlpatterns = [
    path('', IndexView.as_view(), name='index'), #TODO Alterar para Class Based View
    path('unidadeorganizacional/', views.unidadeOrganizacionalList, name='unidade_organizacional'),
    path('unidadeorganizacional_create/', UnidadeOrganizacionalCreateView.as_view()),
    path('unidadeorganizacional/<pk>/', UnidadeOrganizacionalDetailView.as_view()),
    path('unidadeorganizacional/<pk>/update', UnidadeOrganizacionalUpdateView.as_view()),
    path('unidadeorganizacional/<pk>/delete/', UnidadeOrganizacionalDeleteView.as_view()),
]
