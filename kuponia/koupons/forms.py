from django import forms
from django.forms import extras

GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Nombre', required=True)
    last_name = forms.CharField(max_length=30, label='Apellido', required=True)
    birthdate = forms.DateField(widget=extras.SelectDateWidget(years=range(1950,2005)), label='Fecha Nacimiento', required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, initial='M', label='Sexo', required=True)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
	user.birthdate = self.cleaned_data['birthdate']
	user.gender = self.cleaned_data['gender']
        user.save()
