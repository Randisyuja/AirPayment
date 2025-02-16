import uuid
from django.db import models
from AirPayment.pengguna.models import Rumah, Pelanggan, Akun
from AirPayment.transaksi.choices import MonthChoices
from django.utils.translation import gettext_lazy as _


class Periode(models.Model):
    tahun = models.CharField(max_length=4, unique=True, null=False, blank=False)

    def __str__(self):
        return f"Periode {self.tahun}"


class Pembayaran(models.Model):
    nomor_pembayaran = models.CharField(max_length=20, unique=True, editable=False, verbose_name=_("Nomor Pembayaran"))
    pelanggan = models.ForeignKey(
        Pelanggan, on_delete=models.CASCADE, verbose_name=_("Pelanggan")
    )
    tanggal_pembayaran = models.DateTimeField(auto_now_add=True, verbose_name=_("Tanggal Pembayaran"))
    bulan = models.CharField(max_length=20, choices=MonthChoices, verbose_name=_("Bulan"))
    periode = models.ForeignKey(
        Periode, on_delete=models.DO_NOTHING, verbose_name=_("Periode")
    )
    jumlah = models.IntegerField(default=50000, verbose_name=_("Jumlah"))
    metode_pembayaran = models.CharField(
        max_length=30,
        choices=[
            ('transfer', _("Transfer Bank")),
            ('tunai', _("Tunai")),
        ],
        verbose_name=_("Metode Pembayaran")
    )
    keterangan = models.TextField(blank=True, null=True, verbose_name=_("Keterangan"))
    nomor_hp_pelanggan = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name=_("Nomor HP Pelanggan"),
    )
    alamat = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name=_("Alamat"),
    )
    kasir = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        verbose_name=_("Kasir")
    )

    class Meta:
        verbose_name = _("Pembayaran")
        verbose_name_plural = _("Pembayaran")
        ordering = ['-tanggal_pembayaran']

    def __str__(self):
        return f"{self.pelanggan} {self.nomor_pembayaran} - {self.jumlah}"

    def save(self, *args, **kwargs):
        if not self.nomor_pembayaran:
            unique_id = int(str(uuid.uuid4().int)[:10])  # Ambil 6 karakter pertama dari UUID dengan tipe data integer
            self.nomor_pembayaran = f"AB{unique_id}"

        super().save(*args, **kwargs)
