from django.db import models
from django.conf import settings
from django.utils import timezone



class Post(models.Model):
    description = models.CharField(
        max_length=200,
        verbose_name='Описание',
        null=False
    )
    image = models.ImageField(
        verbose_name='Фото',
        null=False,
        blank=True,
        upload_to='post_images'
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='Автор',
        related_name='posts',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время",
        null=True
    )
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
