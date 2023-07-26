from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.exceptions import PermissionDenied

import requests as req
import os

from .serializers import PurchaseHistorySerializer
from .models import PurchaseHistory
from .permissions import IsUserAuthenticated

# Create your views here.
class ProductAPIView(ListAPIView):
    permission_classes = (IsUserAuthenticated,)
    template_name = 'core/catalogue.html'
    renderer_classes = [TemplateHTMLRenderer]

    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get('AUTH_COOKIE') is None and request.COOKIES.get('USERNAME') is None:
            return redirect(reverse('auth_login'))
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        search_query = request.GET.get('q')
        if search_query:
            data = req.get(os.environ.get('SS_API_URL') + 'barang?q=' + search_query).json()
        else:
            data = req.get(os.environ.get('SS_API_URL') + 'barang').json()
        
        paginator = Paginator(data['data'], 10)

        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        
        try:
            data = paginator.page(page)
        except(EmptyPage, InvalidPage):
            data = paginator.page(paginator.num_pages)
        
        context = {
            'data': data
        }
        return Response(context, status=status.HTTP_200_OK)
    
class ProductDetailAPIView(ListAPIView):
    permission_classes = (IsUserAuthenticated,)
    template_name = 'core/product-details.html'
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = PurchaseHistorySerializer

    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get('AUTH_COOKIE') is None and request.COOKIES.get('USERNAME') is None:
            return redirect(reverse('auth_login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        data = req.get(os.environ.get('SS_API_URL') + 'barang/' + pk).json()
        data = data['data']
        return Response({
            'data': data
        }, status=status.HTTP_200_OK)

    def post(self, request, pk):
        stok = request.POST.get('stok')
        if stok is None or stok == '' or int(stok) < 1:
            messages.error(request, 'Stok tidak boleh kosong')
            return redirect(reverse('api-product-details', args=[pk]))
        
        username = request.COOKIES.get('USERNAME')
        if username is None:
            return redirect(reverse('auth_login'))
        user = User.objects.get(username=username)

        data = req.get(os.environ.get('SS_API_URL') + 'barang/' + pk).json()['data']
        
        if data['stok'] < int(stok) or int(stok) <= 0:
            messages.error(request, 'Stok tidak cukup')
            return redirect(reverse('api-product-details', args=[pk]))
        data['stok'] = int(data['stok']) - int(stok)

        new_prod = PurchaseHistory.objects.create(
            user=user,
            product=data['nama'],
            price=data['harga'] * int(stok),
            total=stok,
        )
        new_prod.save()
        
        if new_prod is not None:
            data = req.put(os.environ.get('SS_API_URL') + 'barang/' + pk, json=data).json()
            if data['status'] == 'error':
                messages.error(request, data['message'])     
                return redirect(reverse('api-product-details', args=[pk]))
            else:
                messages.success(request, 'Berhasil membeli barang')
                return redirect(reverse('api-product'))
        
        messages.error(request, 'Gagal membeli barang')
        return redirect(reverse('api-product-details', args=[pk]))
    
class PurchaseHistoryAPIView(ListAPIView):
    permission_classes = (IsUserAuthenticated,)
    template_name = 'core/purchase-history.html'
    renderer_classes = [TemplateHTMLRenderer]
    
    queryset = PurchaseHistory.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get('AUTH_COOKIE') is None and request.COOKIES.get('USERNAME') is None:
            return redirect(reverse('auth_login'))
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        username = request.COOKIES.get('USERNAME')
        user = User.objects.get(username=username)

        history = PurchaseHistory.objects.filter(user=user).order_by('-date')
        
        paginator = Paginator(history, 10)

        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1

        try:
            history = paginator.page(page)
        except(EmptyPage, InvalidPage):
            history = paginator.page(paginator.num_pages)

        context = {
            'data': history
        }
        return Response(context, status=status.HTTP_200_OK)
    
    