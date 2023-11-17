from django.db import models
from django.utils import timezone


class ContactInfo(models.Model):
    text = models.TextField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    additional_phone_number = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'


class Appealing(models.Model):  # Müraciət
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.full_name} - {self.email}'

    class Meta:
        verbose_name = 'Appealing'
        verbose_name_plural = 'Appealings'
