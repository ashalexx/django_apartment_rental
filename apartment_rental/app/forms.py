from django import forms
from .models import People


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['people_id',
                  'first_name',
                  'last_name',
                  'middle_name']
        labels = {
            'people_id': 'ID арендатора',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество'
        }
