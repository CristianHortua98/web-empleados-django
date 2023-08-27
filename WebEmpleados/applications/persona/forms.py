from django import forms
from .models import Empleado

class EmpleadoUpdateForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'hoja_vida', 'avatar']
        #fields = ('__all__')

        widgets = {

            'first_name': forms.TextInput(attrs={'placeholder':'Escriba su nombre', 'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Escriba su apellido', 'class':'form-control'}),
            'job': forms.Select(attrs={'class':'form-control'}, choices=Empleado.job_choices),
            'departamento': forms.Select(attrs={'class':'form-control'}),
            'habilidades': forms.CheckboxSelectMultiple(),
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'hoja_vida': forms.Textarea(attrs={'class':'form-control'})
        }

    '''
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        
        return cantidad
    '''