from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from AirPayment.pengguna.choices import StatusChoice, RoleChoice


class Pelanggan(models.Model):
    nama = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    nomor_hp = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    rumah = models.OneToOneField(
        'Rumah',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nama


class Rumah(models.Model):
    alamat = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    status = models.CharField(
        max_length=25,
        choices=StatusChoice,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.alamat

    def save(self, *args, **kwargs):
        self.alamat = self.alamat.upper()
        super().save(*args, **kwargs)


class Akun(AbstractUser):
    nama = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    nomor_hp = models.CharField(
        max_length=25,
        null=False,
        blank=False
    )

    role = models.CharField(
        max_length=10,
        choices=RoleChoice
    )

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Ambil request dari kwargs
        if request and not request.user.is_superuser:
            raise ValidationError("Only superusers can modify this field.")
        super().save(*args, **kwargs)
