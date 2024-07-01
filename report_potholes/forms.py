from django import forms
from .models import Pothole
from django.core.exceptions import ValidationError

class PotholeForm(forms.ModelForm):
    class Meta:
        model = Pothole
        fields = ['reported_by', 'phone', 'photo', 'latitude', 'longitude']
        labels = {
            'reported_by': 'Reportado por',
            'phone': 'Teléfono',
            'photo': 'Foto',
            'latitude': 'Latitud',
            'longitude': 'Longitud',
        }
        widgets = {
            'reported_by': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }


class ProyectForm(forms.ModelForm):
    year_management = forms.ChoiceField(choices=[(r,r) for r in range(2000, 2030)],label='Gestión', widget=forms.Select(), required=False)

    class Meta:
        model = Pothole
        fields = ['title','photo','description','category', 'year_management', 'latitude', 'longitude']
        labels = {
            'title': 'Titúlo',
            'category': 'Categoria',
            'photo': 'Foto',
            'latitude': 'Latitud',
            'longitude': 'Longitud',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'year_management': forms.Select(attrs={'class': 'form-control','required': 'required'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly','required': 'required'},),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly','required': 'required'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')

        if latitude is None or longitude is None:
            raise ValidationError("Los campos de latitud y longitud son obligatorios.")

        return cleaned_data
    

class ProyectFormPublic(forms.ModelForm):
    # year_management = forms.ChoiceField(choices=[(r,r) for r in range(2000, 2030)],label='Gestión', widget=forms.Select(), required=False)

    class Meta:
        model = Pothole
        fields = ['title','photo','description','location','province','municipality','discovery_date','latitude', 'longitude']
        labels = {
            'title': 'Titúlo',
            'photo': 'Foto',
            'latitude': 'Latitud',
            'longitude': 'Longitud',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'municipality': forms.TextInput(attrs={'class': 'form-control'}),
            'discovery_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly','required': 'required'},),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly','required': 'required'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')

        if latitude is None or longitude is None:
            raise ValidationError("Los campos de latitud y longitud son obligatorios.")

        return cleaned_data