from django import forms

from mail_sending.models import Client, Message


class ClientForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')
    second_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Отчество')
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Комментарий',
                              required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Электронная почта')

    class Meta:
        model = Client
        fields = ['name', 'surname', 'second_name', 'comment', 'email']


class MessageForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Тема сообщения')
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Текст сообщения')

    class Meta:
        model = Message
        fields = ['title', 'message']
