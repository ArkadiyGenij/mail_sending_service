from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms
from django.forms import DateTimeInput
from django.utils.timezone import now

from mail_sending import models
from mail_sending.models import Client, Message, Mailing


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'first_send_date':
                field.widget = DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'second_name', 'comment', 'email']


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'message']


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['first_send_date', 'periodicity', 'clients', 'message']

    def clean(self):
        cleaned_data = super().clean()
        first_send_date = cleaned_data.get('first_send_date')
        if first_send_date:
            current_time = now()

            if first_send_date <= current_time:
                clients = Client.objects.all()

                cleaned_data['clients'] = clients

        return cleaned_data
