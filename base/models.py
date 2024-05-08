from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class HelpDeskUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "HelpDesk сотрудник"

    def __str__(self):
            return f'{self.username}'


class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='ФИО')


    class Meta:
        verbose_name_plural = "Преподаватели и Сотрудники"

    def __str__(self):
        return f'{self.full_name}'
    

class Auditorium(models.Model):
    number = models.CharField(max_length=100, verbose_name='Номер аудитории')

    def __str__(self):
        return self.number


class HelpDeskRequest(models.Model):
    auditorium_number = models.ForeignKey(Auditorium, on_delete=models.CASCADE, verbose_name='Аудитория')
    description = models.TextField(verbose_name='Описание')
    creator = models.CharField(max_length=100, verbose_name='От')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефонный номер')
    handler = models.ForeignKey(HelpDeskUser, related_name='handled_requests', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Заявку принял')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')

    NEW = 'NEW'
    IN_PROCESS = 'IN_PROCESS'
    CLOSED = 'CLOSED'

    STATUS_CHOICES = [
        (NEW, 'Новая'),
        (IN_PROCESS, 'В обработке'),
        (CLOSED, 'Закрыта'),
    ]
    status = models.CharField(
         max_length=20,
         choices=STATUS_CHOICES,
         default=NEW,
        verbose_name='Статус'
    )
    
    def get_auditorium_url(self):
        return reverse('auditorium_detail', args=[self.auditorium.number])

    class Meta:
        verbose_name_plural = "Заявки HelpDesk"

    def __str__(self):
        return f"Заявка №{self.id} от {self.creator}, статус {self.status}"
