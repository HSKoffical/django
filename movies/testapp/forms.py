from django import forms
from testapp.models import movies_db
class movies_form(forms.ModelForm):
    name=forms.CharField()
    actor=forms.CharField()
    actress=forms.CharField()
    year=forms.IntegerField()
    rating=forms.IntegerField()
    class Meta:
        model=movies_db
        fields='__all__'
