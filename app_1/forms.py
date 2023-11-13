from django import forms
from django.core.exceptions import ValidationError

class Formulario1(forms.Form):
    DIAS_SEMANA_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    fecha_inicio = forms.DateField(label='Fecha de inicio', widget=forms.DateInput(), help_text="Debe tener formato: dd/mm/YYYY y ser menor que la fecha final", input_formats=['%d/%m/%Y'])
    fecha_fin = forms.DateField(label='Fecha final', widget=forms.DateInput(), help_text="Debe tener formato: dd/mm/YYYY", input_formats=['%d/%m/%Y'])
    dias_semana = forms.MultipleChoiceField(label='Dias de la semana', choices=DIAS_SEMANA_CHOICES, widget=forms.CheckboxSelectMultiple, help_text="Debe elegir al menos un día y máximo 3")
    correo_electronico = forms.EmailField(max_length=100, help_text="El correo electrónico debe escribirse de esta manera: XXX@iesmartinezm.es")

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        dias_semana = cleaned_data.get('dias_semana')
        correo_electronico = cleaned_data.get('correo_electronico')

        # Realiza validaciones personalizadas si es necesario
        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        if not dias_semana:
            raise ValidationError("Debe elegir al menos un día")
        if len(dias_semana) > 3:
            raise ValidationError("No puede elegir más de 3 días")
        if not correo_electronico.endswith('@iesmartinezm.es'):
            raise ValidationError("El correo electrónico debe acabar en @iesmartinezm.es")
