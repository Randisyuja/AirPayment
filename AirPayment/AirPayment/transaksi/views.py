from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AirPayment.transaksi.models import Pembayaran, Periode


class PembayaranListView(ListView):
    model = Pembayaran
    template_name = 'transaksi/pembayaran-list.html'
    context_object_name = 'pembayaran_list'


class PembayaranCreateView(CreateView):
    model = Pembayaran
    template_name = 'transaksi/add-pembayaran.html'
    fields = '__all__'
    success_url = reverse_lazy('pembayaran-list')


class PembayaranUpdateView(UpdateView):
    model = Pembayaran
    template_name = 'transaksi/edit-pembayaran.html'
    fields = '__all__'
    success_url = reverse_lazy('pembayaran-list')


class PembayaranDeleteView(DeleteView):
    model = Pembayaran
    template_name = 'transaksi/delete-pembayaran.html'
    success_url = reverse_lazy('pembayaran-list')


class PeriodeListView(ListView):
    model = Periode
    template_name = 'transaksi/periode-list.html'
    context_object_name = 'periode_list'


class PeriodeCreateView(CreateView):
    model = Periode
    template_name = 'transaksi/add-periode.html'
    fields = '__all__'
    success_url = reverse_lazy('periode-list')


class PeriodeUpdateView(UpdateView):
    model = Periode
    template_name = 'transaksi/update-periode.html'
    fields = '__all__'
    success_url = reverse_lazy('periode-list')


class PeriodeDeleteView(DeleteView):
    model = Periode
    template_name = 'transaksi/delete-periode.html'
    success_url = reverse_lazy('periode-list')



