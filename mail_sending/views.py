from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mail_sending.forms import ClientForm
from mail_sending.models import Client


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
