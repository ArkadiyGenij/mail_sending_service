from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mail_sending.forms import ClientForm, MessageForm, MailingForm
from mail_sending.models import Client, Message, Mailing


# Create your views here.
class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
    }


class ClientDetailView(DetailView):
    model = Client
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
    }


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
        'form_name': 'Добавление клиента'
    }
    success_url = reverse_lazy('mail_sending:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
        'form_name': 'Редактирование клиента'
    }
    success_url = reverse_lazy('mail_sending:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mail_sending:client_list')


class MessageListView(ListView):
    model = Message
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
    }


class MessageDetailView(DetailView):
    model = Message
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
    }


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
        'form_name': 'Добавление сообщения'
    }
    success_url = reverse_lazy('mail_sending:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
        'form_name': 'Редактирование сообщения'
    }
    success_url = reverse_lazy('mail_sending:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mail_sending:message_list')


class MailingListView(ListView):
    model = Mailing
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
    }


class MailingDetailView(DetailView):
    model = Mailing
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
    }


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
        'form_name': 'Создание рассылки'
    }
    success_url = reverse_lazy('mail_sending:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {
        'title': 'Панель администратора',
        'page_name': 'Панель администратора',
        'form_name': 'Редактирование рассылки'
    }
    success_url = reverse_lazy('mail_sending:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mail_sending:mailing_list')
