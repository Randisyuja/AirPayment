from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from AirPayment.pengguna.models import Pelanggan, Rumah
from AirPayment.pengguna.forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home.html')


class PelangganListView(ListView):
    model = Pelanggan
    template_name = 'pelanggan/pelanggan-list.html'
    context_object_name = 'pelanggan_list'


class PelangganCreateView(CreateView):
    model = Pelanggan
    template_name = 'pelanggan/add-pelanggan-form.html'
    fields = ['nama', 'nomor_hp', 'rumah']  # Field yang akan ditampilkan dalam form
    success_url = reverse_lazy('pelanggan-list')  # Redirect setelah berhasil menambahkan data


class PelangganUpdateView(UpdateView):
    model = Pelanggan
    template_name = 'pelanggan/update-pelanggan.html'
    fields = ['nama', 'nomor_hp', 'rumah']  # Field yang akan ditampilkan dalam form
    success_url = reverse_lazy('pelanggan-list')  # Redirect setelah berhasil memperbarui data


class PelangganDeleteView(DeleteView):
    model = Pelanggan
    template_name = 'pelanggan/delete-pelanggan.html'
    success_url = reverse_lazy('pelanggan-list')  # Redirect setelah berhasil menghapus data


class RumahCreateView(CreateView):
    model = Rumah
    template_name = 'rumah/add-rumah.html'
    fields = ['alamat', 'status']  # Field yang akan ditampilkan dalam form
    success_url = reverse_lazy('rumah-list')  # Redirect setelah berhasil menambahkan data


class RumahUpdateView(UpdateView):
    model = Rumah
    template_name = 'rumah/update-rumah.html'
    fields = ['alamat', 'status']  # Field yang akan ditampilkan dalam form
    success_url = reverse_lazy('rumah-list')  # Redirect setelah berhasil memperbarui data


class RumahDeleteView(DeleteView):
    model = Rumah
    template_name = 'rumah/delete-rumah.html'
    success_url = reverse_lazy('rumah-list')  # Redirect setelah berhasil menghapus data


class RumahListView(ListView):
    model = Rumah
    template_name = 'rumah/rumah-list.html'
    context_object_name = 'rumah_list'


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect ke homepage jika sudah login

    if request.method == 'POST':
        form = SignUpForm(request.POST)  # Correct usage
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'akun/signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect jika sudah login
        else:
            form = LoginForm()
        return render(request, 'akun/login.html', {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect ke halaman utama
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'akun/login.html')  # Tampilkan kembali form login


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)  # Hapus sesi pengguna
        messages.success(request, "You have successfully logged out.")
        return redirect('login')  # Redirect ke halaman login
