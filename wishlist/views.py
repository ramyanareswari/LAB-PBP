from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from wishlist.models import BarangWishlist

# Sebuah fungsi yang menerima parameter request dan mengembalikan render(request, "wishlist.html")
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    # name_header = Name.objects.all()
    
    context = {
        'list_barang': data_barang_wishlist,
        'nama':  'Ramya Nareswari'
    }

    return render(request, "wishlist.html", context)

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