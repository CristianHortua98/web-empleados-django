from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = ['titulo', 'subtitulo', 'cantidad']
        #fields = ('__all__')

        widgets = {

            'titulo': forms.TextInput(attrs={'placeholder':'Escribe el titulo', 'class':'form-control'}),
            'subtitulo': forms.TextInput(attrs={'placeholder':'Escribe el subtitulo'}),
            'cantidad': forms.NumberInput(attrs={'min':'5', 'max':'6'})

        }

    '''
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        
        return cantidad
    '''