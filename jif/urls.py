from django.urls import path

from jif.views.index_views import IndexView

from jif.views.instituto_views import (
    InstitutoView,
    InstitutoCreateView,
    InstitutoDetailView,
    InstitutoUpdateView,
    InstitutoDeleteView
)

from jif.views.campus_views import (
    CampusView,
    CampusCreateView,
    CampusDetailView,
    CampusUpdateView,
    CampusDeleteView
)

from jif.views.edicao_views import (
    EdicaoView,
    EdicaoCreateView,
    EdicaoDetailView,
    EdicaoUpdateView,
    EdicaoDeleteView,
    EdicaoCategoriaCreateView,
    EdicaoCategoriaUpdateView,
    EdicaoCategoriaDeleteView,
    EdicaoModalidadeCreateView,
    EdicaoModalidadeUpdateView,
    EdicaoModalidadeDeleteView,
    EdicaoModalidadeProvaCreateView,
)

from jif.views.categoria_views import (
    CategoriaView,
    CategoriaCreateView,
    CategoriaDetailView,
    CategoriaUpdateView,
    CategoriaDeleteView
)

from jif.views.prova_views import (
    ProvaView,
    ProvaCreateView,
    ProvaDetailView,
    ProvaUpdateView,
    ProvaDeleteView
)

from jif.views.etapa_views import (
    EtapaView,
    EtapaCreateView,
    EtapaDetailView,
    EtapaUpdateView,
    EtapaDeleteView
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
    InscricaoModalidadeJSONView,
    InscricaoModalidadeLineJSONView
)

from .views import relatorio_views

from jif.views.usuario_views import UsuarioView


urlpatterns = [
    # Index URL
    path('', IndexView.as_view(), name='index'),
    # Instituto URLs
    path('instituto/', InstitutoView.as_view(), name='instituto'),
    path('instituto_create/', InstitutoCreateView.as_view()),
    path('instituto/<pk>/', InstitutoDetailView.as_view()),
    path('instituto/<pk>/update', InstitutoUpdateView.as_view()),
    path('instituto/<pk>/delete/', InstitutoDeleteView.as_view()),
    # Campus URLs
    path('campus/', CampusView.as_view(), name='campus'),
    path('campus_create/', CampusCreateView.as_view()),
    path('campus/<pk>/', CampusDetailView.as_view()),
    path('campus/<pk>/update', CampusUpdateView.as_view()),
    path('campus/<pk>/delete/', CampusDeleteView.as_view()),
    # Edicao URLs
    path('edicao/', EdicaoView.as_view(), name='edicao'),
    path('edicao_create/', EdicaoCreateView.as_view()),
    path('edicao/<pk>/', EdicaoDetailView.as_view()),
    path('edicao/<pk>/update', EdicaoUpdateView.as_view()),
    path('edicao/<pk>/delete/', EdicaoDeleteView.as_view()),
    path('edicao/categoria/create/<pk>/', EdicaoCategoriaCreateView.as_view()),
    path('edicao/categoria/<pk>/update', EdicaoCategoriaUpdateView.as_view()),
    path('edicao/categoria/<pk>/delete/', EdicaoCategoriaDeleteView.as_view()),
    path('edicao/modalidade/create/<pk>/', EdicaoModalidadeCreateView.as_view()),
    path('edicao/modalidade/<pk>/update', EdicaoModalidadeUpdateView.as_view()),
    path('edicao/modalidade/<pk>/delete/', EdicaoModalidadeDeleteView.as_view()),
    path('edicao/prova/create/<pk>/', EdicaoModalidadeProvaCreateView.as_view()),

    # Categoria URLs
    path('categoria/', CategoriaView.as_view(), name='categoria'),
    path('categoria_create/', CategoriaCreateView.as_view()),
    path('categoria/<pk>/', CategoriaDetailView.as_view()),
    path('categoria/<pk>/update', CategoriaUpdateView.as_view()),
    path('categoria/<pk>/delete/', CategoriaDeleteView.as_view()),
    # Prova URLs
    path('prova/', ProvaView.as_view(), name='prova'),
    path('prova_create/', ProvaCreateView.as_view()),
    path('prova/<pk>/', ProvaDetailView.as_view()),
    path('prova/<pk>/update', ProvaUpdateView.as_view()),
    path('prova/<pk>/delete/', ProvaDeleteView.as_view()),
    # Etapa URLs
    path('etapa/', EtapaView.as_view(), name='etapa'),
    path('etapa_create/', EtapaCreateView.as_view()),
    path('etapa/<pk>/', EtapaDetailView.as_view()),
    path('etapa/<pk>/update', EtapaUpdateView.as_view()),
    path('etapa/<pk>/delete/', EtapaDeleteView.as_view()),
    # Modalidade URLs
    path('modalidade/', ModalidadeView.as_view(), name='modalidade'),
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
    path('inscricao/', InscricaoView.as_view(), name='inscricao'),
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
    path('dadosinscricaomodalidadeLine/', InscricaoModalidadeLineJSONView.as_view(), name='dados_inscricao_modalidadeLine'),
    # Usuário URL
    path('usuario/', UsuarioView.as_view(), name='usuario'),
]
