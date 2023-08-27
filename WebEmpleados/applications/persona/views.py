from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Empleado
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EmpleadoUpdateForm


# Create your views here.

class InicioView(TemplateView):
    template_name = 'inicio.html'

class AdminEmpleadoListView(ListView):
    model = Empleado
    template_name = 'persona/admin-empleados.html'
    context_object_name = 'listaEmpleados'
    ordering = 'first_name'

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'persona/list-empleados.html'
    context_object_name = 'listaEmpleados'
    ordering = 'first_name'

class AreaEmpleadoListView(ListView):
    template_name = 'persona/list-area.html'
    #Filtrar la busqueda por el name de la tabla Departamento
    #queryset = Empleado.objects.filter(departamento__name='Economia y Finanzas')
    context_object_name = 'listAreasEmpleados'

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(departamento__short_name=area)
        return lista
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        context['departamento'] = self.kwargs['shortname']
        return context

class EmpleadosBusquedaListView(ListView):
    template_name = 'persona/busqueda-empleados.html'
    context_object_name = 'listaBusqueda'

    def get_queryset(self):
        if self.request.GET:
            palabraClave = self.request.GET['kword']
            lista = Empleado.objects.filter(first_name=palabraClave)
            return lista
        
class HabilidadesEmpleadoListView(ListView):
    template_name = 'persona/list-habilidades-empleado.html'
    context_object_name = 'listaHabilidades'

    def get_queryset(self):
        idEmpleado = self.kwargs['idEmpleado']
        #Recuperando 1 registro de Empleados
        empleado = Empleado.objects.get(id=idEmpleado)
        habilidades = empleado.habilidades.all()
        return habilidades
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        idEmpleado = self.kwargs['idEmpleado']
        context['empleado'] = Empleado.objects.get(id=idEmpleado)
        return context
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail-empleado.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/agregar-empleado.html'
    #fields = ['first_name', 'last_name', 'job', 'departamento', 'hoja_vida', 'habilidades']
    form_class = EmpleadoUpdateForm
    success_url = reverse_lazy('persona_app:admin-empleado-list')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'persona/editar-empleado.html'
    #fields = ['first_name', 'last_name', 'job', 'departamento', 'hoja_vida', 'habilidades']
    success_url = reverse_lazy('persona_app:admin-empleado-list')
    form_class = EmpleadoUpdateForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #print(request.POST)
        #print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/eliminar-empleado.html'

    success_url = reverse_lazy('persona_app:admin-empleado-list')
