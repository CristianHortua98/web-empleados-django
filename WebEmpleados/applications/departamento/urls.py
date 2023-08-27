from django.urls import path
from .views import *

app_name = "departamento_app"

urlpatterns = [
    path('', DepartamentoPageView.as_view(), name='departamentos-list'),
    path('agregar-departamento/', RegistrarDepartamentoFormView.as_view(), name='departamento-add')
]