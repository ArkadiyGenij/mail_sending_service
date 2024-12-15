from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    surname = models.CharField(max_length=100, verbose_name="фамилия")
    second_name = models.CharField(max_length=100, verbose_name="отчество")
    email = models.EmailField(max_length=100, verbose_name="электронная почта")
    comment = models.TextField(max_length=400, verbose_name="комментарий", null=True, blank=True)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return f"{self.name} {self.surname} {self.second_name}"


class Message(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="тема письма")
    message = models.TextField(max_length=1500, blank=False, null=False, verbose_name="тело письма")

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return self.title


class Mailing(models.Model):
    PERIOD_CHOICES = (
        ('daily', 'раз в день'),
        ('weekly', 'раз в неделю'),
        ('monthly', 'раз в месяц'),
    )

    STATUS_CHOICES = (
        ('draft', 'создана'),
        ('sent', 'отправлена'),
        ('completed', 'завершена'),
    )

    first_send_date = models.DateTimeField(verbose_name="дата и время первой рассылки")
    periodicity = models.CharField(max_length=15, choices=PERIOD_CHOICES, default='daily', verbose_name="периодичность")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft', verbose_name="статус")
    clients = models.ManyToManyField(Client, verbose_name="клиенты")
    message = models.OneToOneField(Message, on_delete=models.CASCADE, verbose_name="cсообщение")

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    def __str__(self):
        return f"{self.status} рассылка: {self.message.title}"


class MailingAttempt(models.Model):
    LAST_ATTEMPT_STATUS_CHOICES = (
        ('success', 'успешно'),
        ('failure', 'не успешно'),
    )

    last_attempt_date = models.DateTimeField()
    attempt_status = models.CharField(max_length=10, choices=LAST_ATTEMPT_STATUS_CHOICES, default='failure')
    response = models.TextField(blank=True, null=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mailing} {self.attempt_status} {self.last_attempt_date}"
