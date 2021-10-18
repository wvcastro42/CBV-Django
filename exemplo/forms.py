from django import forms

from exemplo.models import Cliente

class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

