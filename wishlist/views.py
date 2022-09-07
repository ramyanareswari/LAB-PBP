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