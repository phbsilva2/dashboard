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

from jif.views.atleta_views import (
    AtletaView,
    AtletaCreateView,
    AtletaDetailView,
    AtletaUpdateView,
    AtletaDeleteView
)

from jif.views.inscricao_views import (
    InscricaoView,
    InscricaoCreateView,
    InscricaoDetailView,
    InscricaoUpdateView,
    InscricaoDeleteView
)

from jif.views.grafico_views import (
    GraficoView,
    InscricaoCampusJSONView,
    InscricaoModalidadeJSONView
)

from .views import relatorio_views


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
    # Atleta URLs
    path('atleta/', AtletaView.as_view(), name='atleta_list'),
    path('atleta_create/', AtletaCreateView.as_view()),
    path('atleta/<pk>/', AtletaDetailView.as_view()),
    path('atleta/<pk>/update', AtletaUpdateView.as_view()),
    path('atleta/<pk>/delete/', AtletaDeleteView.as_view()),
    # Inscrição URLs
    path('inscricao/', InscricaoView.as_view(), name='inscricao_list'),
    path('inscricao_create/', InscricaoCreateView.as_view()),
    path('inscricao/<pk>/', InscricaoDetailView.as_view()),
    path('inscricao/<pk>/update', InscricaoUpdateView.as_view()),
    path('inscricao/<pk>/delete/', InscricaoDeleteView.as_view()),
    # Relatório URLs
    path('atletacampus/', relatorio_views.atleta_campus, name='atleta_campus'),
    path('atletamodalidade/', relatorio_views.atleta_modalidade, name='atleta_modalidade'),
    path('atletatipomodalidade/', relatorio_views.atleta_tipo_modalidade, name='atleta_tipo_modalidade'),
    path('inscricoesatletas/', relatorio_views.inscricoes_atletas, name='inscricoes_atletas'),
    path('fichainscricao/<int:uo_id>/<int:modalidade_id>', relatorio_views.fichaisncricao, name='ficha_inscricao'),
    # Gráfico URLs
    path('grafico/', GraficoView.as_view(), name='grafico'),
    path('dadosinscricaocampus/', InscricaoCampusJSONView.as_view(), name='dados_inscricao_campus'),
    path('dadosinscricaomodalidade/', InscricaoModalidadeJSONView.as_view(), name='dados_inscricao_modalidade'),
]
