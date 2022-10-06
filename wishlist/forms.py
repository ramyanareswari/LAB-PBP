from django import forms
from wishlist.models import BarangWishlist
from django.forms import NumberInput, TextInput

class CreateNew(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        fields = ['nama_barang', 'harga_barang', 'deskripsi']

        widgets = {
            'nama_barang': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Insert product name..',
                'required': 'False'
                }),
            'harga_barang': NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Insert task description..',
                'required': 'False'
                }),
            'deskripsi': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Insert description',
                'required': 'False'
                }),
        }
