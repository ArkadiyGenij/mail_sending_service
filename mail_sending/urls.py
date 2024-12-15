from django.urls import path

from mail_sending import views

app_name = 'mail_sending'
urlpatterns = [
    path('', views.index, name='index'),
]
