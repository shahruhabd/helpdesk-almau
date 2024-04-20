from django.db import models
from django.contrib.auth.models import User

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


class HelpDeskRequest(models.Model):
    auditorium_number = models.CharField(max_length=100, verbose_name='Аудитория')
    description = models.TextField(verbose_name='Описание')
    creator = models.ForeignKey(Lecturer, related_name='created_requests', on_delete=models.CASCADE, verbose_name='От')
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

    class Meta:
        verbose_name_plural = "Заявки HelpDesk"

    def __str__(self):
        return f"Заявка №{self.id} от {self.creator}, статус {self.status}"
