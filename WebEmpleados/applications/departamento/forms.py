from django import forms

class NuevoDepartamentoForm(forms.Form):
    
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el departamento...'}))
    shortname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre corto...'}))
