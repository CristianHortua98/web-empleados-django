from django.http import HttpResponse
from django.shortcuts import render
from .forms import NuevoDepartamentoForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from applications.persona.models import Empleado
from .models import Departamento

class DepartamentoPageView(ListView):
    model = Departamento
    context_object_name = 'departamentos'
    template_name = 'departamento/departamentos.html'

class RegistrarDepartamentoFormView(FormView):
    template_name = 'departamento/agregar-departamento.html'
    form_class = NuevoDepartamentoForm
    success_url = reverse_lazy('departamento_app:departamento-add')


    def form_valid(self, form):
        print('******************Estamos en el Form Valid*****************')
        
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname']
        )

        depa.save()
        
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            full_name = nombre + ' ' + apellidos,
            job = '1',
            departamento =  depa
        )


        return super().form_valid(form)
