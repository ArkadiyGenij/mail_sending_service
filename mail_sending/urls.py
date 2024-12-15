from django.urls import path

from mail_sending.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView

app_name = 'mail_sending'
urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/details/<int:pk>', ClientDetailView.as_view(), name='client_details'),
    path('clients/add', ClientCreateView.as_view(), name='client_create'),
    path('clients/edit/<int:pk>', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
]
