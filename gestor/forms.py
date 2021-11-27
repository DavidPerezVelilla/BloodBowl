from django.forms import ModelForm
from gestor.models import Equipo
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class EquipoForm(ModelForm):
    
    class Meta:
        model = Equipo
        fields = '__all__'
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('Nombre', css_class='form-group col-md-6 mb-0'),
                Column('Raza', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('Descripcion', css_class='form-group col-md-6 mb-0'),
                Column('Imagen', css_class='form-group col-md-6 mb-0'),
                css_class='form-row my-2'
            ),
            Submit('submit', 'Enviar')
        )

