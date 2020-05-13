from django.urls import path

from jif.views.index_views import IndexView

from jif.views.unidade_organizacional_views import (
    UnidadeOrganizacionalView,
    UnidadeOrganizacionalCreateView,
    UnidadeOrganizacionalDetailView,
    UnidadeOrganizacionalUpdateView,
    UnidadeOrganizacionalDeleteView,
)


urlpatterns = [
    # Index URL
    path('', IndexView.as_view(), name='index'),
    # Unidade Organizacional URLs
    path('unidadeorganizacional/', UnidadeOrganizacionalView.as_view(), name='unidade_organizacional_list'),
    path('unidadeorganizacional_create/', UnidadeOrganizacionalCreateView.as_view()),
    path('unidadeorganizacional/<pk>/', UnidadeOrganizacionalDetailView.as_view()),
    path('unidadeorganizacional/<pk>/update', UnidadeOrganizacionalUpdateView.as_view()),
    path('unidadeorganizacional/<pk>/delete/', UnidadeOrganizacionalDeleteView.as_view()),
]
