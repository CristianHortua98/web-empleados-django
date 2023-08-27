from django.urls import path
from .views import *

app_name = "persona_app"

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('lista-empleados/', EmpleadoListView.as_view(), name='empleado-list'),
    path('admin-empleados/', AdminEmpleadoListView.as_view(), name='admin-empleado-list'),
    path('lista-areas/<shortname>', AreaEmpleadoListView.as_view(), name='area-empleado-list'),
    path('search-empleado/', EmpleadosBusquedaListView.as_view(), name='search-empleado'),
    path('lista-habilidades-empleado/<int:idEmpleado>/', HabilidadesEmpleadoListView.as_view(), name='empleado-habilidades-list'),
    path('detalle-empleado/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado-detail'),
    path('agregar-empleado/', EmpleadoCreateView.as_view(), name='empleado-add'),
    path('editar-empleado/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado-edit'),
    path('eliminar-empleado/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado-delete')
]