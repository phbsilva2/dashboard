from django.urls import path

from .views import (
    IndexView,
    UnidadeOrganizacionalView,
    UnidadeOrganizacionalCreateView,
    UnidadeOrganizacionalDetailView,
    UnidadeOrganizacionalUpdateView,
    UnidadeOrganizacionalDeleteView,
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('unidadeorganizacional/', UnidadeOrganizacionalView.as_view(), name='unidade_organizacional_list'),
    path('unidadeorganizacional_create/', UnidadeOrganizacionalCreateView.as_view()),
    path('unidadeorganizacional/<pk>/', UnidadeOrganizacionalDetailView.as_view()),
    path('unidadeorganizacional/<pk>/update', UnidadeOrganizacionalUpdateView.as_view()),
    path('unidadeorganizacional/<pk>/delete/', UnidadeOrganizacionalDeleteView.as_view()),
]
