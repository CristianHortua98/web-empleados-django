from django.urls import path
from .views import HomeView, HomeListView, HomeCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('list/', HomeListView.as_view(), name='list'),
    path('create/', HomeCreateView.as_view(), name='create')

]