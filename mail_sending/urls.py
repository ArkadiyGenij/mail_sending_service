from django.urls import path

from mail_sending.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView, \
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingListView, \
    MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView

app_name = 'mail_sending'
urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/details/<int:pk>', ClientDetailView.as_view(), name='client_details'),
    path('clients/add', ClientCreateView.as_view(), name='client_create'),
    path('clients/edit/<int:pk>', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/details/<int:pk>', MessageDetailView.as_view(), name='message_details'),
    path('messages/add', MessageCreateView.as_view(), name='message_create'),
    path('messages/edit/<int:pk>', MessageUpdateView.as_view(), name='message_edit'),
    path('messages/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/details/<int:pk>', MailingDetailView.as_view(), name='mailing_details'),
    path('mailings/add', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/edit/<int:pk>', MailingUpdateView.as_view(), name='mailing_edit'),
    path('mailings/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
]
