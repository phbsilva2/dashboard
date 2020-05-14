from django.urls import path

from jif.views.index_views import IndexView

from jif.views.unidade_organizacional_views import (
    UnidadeOrganizacionalView,
    UnidadeOrganizacionalCreateView,
    UnidadeOrganizacionalDetailView,
    UnidadeOrganizacionalUpdateView,
    UnidadeOrganizacionalDeleteView,
)

from jif.views.tipo_modalidade_views import (
    TipoModalidadeView,
    TipoModalidadeCreateView,
    TipoModalidadeDetailView,
    TipoModalidadeUpdateView,
    TipoModalidadeDeleteView
)

from jif.views.modalidade_views import (
    ModalidadeView,
    ModalidadeCreateView,
    ModalidadeDetailView,
    ModalidadeUpdateView,
    ModalidadeDeleteView
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
    # Tipo de Modalidade URLs
    path('tipomodalidade/', TipoModalidadeView.as_view(), name='tipo_modalidade_list'),
    path('tipomodalidade_create/', TipoModalidadeCreateView.as_view()),
    path('tipomodalidade/<pk>/', TipoModalidadeDetailView.as_view()),
    path('tipomodalidade/<pk>/update', TipoModalidadeUpdateView.as_view()),
    path('tipomodalidade/<pk>/delete/', TipoModalidadeDeleteView.as_view()),
    # Modalidade URLs
    path('modalidade/', ModalidadeView.as_view(), name='modalidade_list'),
    path('modalidade_create/', ModalidadeCreateView.as_view()),
    path('modalidade/<pk>/', ModalidadeDetailView.as_view()),
    path('modalidade/<pk>/update', ModalidadeUpdateView.as_view()),
    path('modalidade/<pk>/delete/', ModalidadeDeleteView.as_view()),
]
