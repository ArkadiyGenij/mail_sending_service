from django import forms

from mail_sending.models import Client


class ClientForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')
    second_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Отчество')
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Комментарий', required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Электронная почта')

    class Meta:
        model = Client
        fields = ['name', 'surname', 'second_name', 'comment', 'email']
