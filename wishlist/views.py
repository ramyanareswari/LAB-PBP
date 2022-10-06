from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from wishlist.models import BarangWishlist
import json



# Sebuah fungsi yang menerima parameter request dan mengembalikan render(request, "wishlist.html")
@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    
    context = {
        'list_barang': data_barang_wishlist,
        'nama':  'Ramya Nareswari',
    }

    return render(request, "wishlist.html", context)

def show_wishlist_ajax(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    
    context = {
        'list_barang': data_barang_wishlist,
        'nama':  'Ramya Nareswari',
    }

    return render(request, "wishlist_ajax.html", context)

#  AJAX view which returns a JSON object with boolean from the username exists query
def add_wishlist(request):
    if request.method == 'POST':
        nama_barang = request.POST['nama_barang']
        harga_barang = request.POST['harga_barang']
        deskripsi = request.POST['deskripsi']
        wishlist_obj = BarangWishlist(
            nama_barang=nama_barang,
            harga_barang=harga_barang,
            deskripsi=deskripsi)
        wishlist_obj.save()
        return JsonResponse()
    return render(request, 'wishlist_ajax.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist"))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

## Return Data by ID
def show_json_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")