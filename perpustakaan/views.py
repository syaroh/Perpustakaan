from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.form import FormBuku
from django.contrib import messages

def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    
    messages.success(request, "Data Berhasil Dihapus!")
    return redirect('buku')

def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbarui...!",)
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)


def buku(request):
    # select * from buku where jumlah=90
    # books = Buku.objects.filter(jumlah=80)
    #select *from buku where kelompok_id produktif
    books = Buku.objects.all()# filter(kelompok_id__nama='produktif')[:3] #limit
    
    konteks = {
        'books' : books,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')

def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data Berhasil Disimpan....!"
            
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
        
    else:
        form = FormBuku()
    
        konteks = {
        'form' : form,
    } 
    return render(request, 'tambah-buku.html', konteks)
