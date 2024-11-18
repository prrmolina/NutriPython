from django.urls import path
from .views import cadastrar_usuario
from django.urls import path, include
from .views import index

urlpatterns = [
    path('cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
]
urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    # outras URLs
]


urlpatterns = [
    path('', index, name='index'),
]