from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def buku(request):
    return HttpResponse('halaman buku')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
]
