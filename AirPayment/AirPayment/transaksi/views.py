from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
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
    fields = ['pelanggan', 'bulan', 'periode', 'jumlah', 'metode_pembayaran', 'keterangan']
    success_url = reverse_lazy('pembayaran-list')

    def form_valid(self, form):
        pembayaran = form.save(commit=False)  # Jangan langsung simpan ke database
        pembayaran.kasir = self.request.user.nama  # Ambil nama user yang sedang login
        pembayaran.nomor_hp_pelanggan = pembayaran.pelanggan.nomor_hp  # Set nomor HP otomatis
        pembayaran.alamat = pembayaran.pelanggan.rumah.alamat  # Set alamat otomatis
        pembayaran.save()  # Simpan ke database
        return super().form_valid(form)


class PembayaranUpdateView(UpdateView):
    model = Pembayaran
    template_name = 'transaksi/edit-pembayaran.html'
    fields = '__all__'
    success_url = reverse_lazy('pembayaran-list')


class PembayaranDeleteView(DeleteView):
    model = Pembayaran
    template_name = 'transaksi/delete-pembayaran.html'
    success_url = reverse_lazy('pembayaran-list')


class DetailPembayaran(DetailView):
    model = Pembayaran
    template_name = 'transaksi/detail-transaksi.html'

    def get_object(self):
        return get_object_or_404(Pembayaran, id=self.kwargs['pk'])


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
