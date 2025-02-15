from django.contrib import admin
from AirPayment.pengguna.models import Pelanggan, Rumah, Akun


# Register your models here.
class PelangganAdmin(admin.ModelAdmin):
    fields = ['nama', 'nomor_hp', 'rumah']
    list_display = ['nama', 'nomor_hp', 'rumah']
    search_fields = ['nama', 'nomor_hp', 'rumah__alamat']
    ordering = ['rumah']


admin.site.register(Pelanggan, PelangganAdmin)


class RumahAdmin(admin.ModelAdmin):
    fields = ['alamat', 'status']
    list_display = ['alamat', 'status']
    list_filter = ['status']
    search_fields = ['alamat', 'status']
    ordering = ['alamat']


admin.site.register(Rumah, RumahAdmin)


class AkunAdmin(admin.ModelAdmin):
    fields = ['nama', 'nomor_hp', 'role']
    list_display = ['username', 'nama', 'nomor_hp', 'role']
    list_filter = ['role']
    search_fields = ['nama', 'nomor_hp', 'role']
    ordering = ['nama']


admin.site.register(Akun, AkunAdmin)
