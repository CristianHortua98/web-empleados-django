from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from .models import Prueba
from .forms import PruebaForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "home/home.html"

class HomeListView(ListView):
    template_name = "home/list.html"
    model = Prueba

class HomeCreateView(CreateView):
    template_name = "home/create.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/home'