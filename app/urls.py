from app.views import agregar, editar, eliminar, index
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', index, name='index'),
    path('agregar/', agregar, name='agregar'),
    path('editar/<int:id>/', editar, name='editar'),
    path('eliminar/<int:id>/', eliminar, name='eliminar'),
]
