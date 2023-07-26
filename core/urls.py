from django.urls import path

from .views import ProductAPIView, ProductDetailAPIView, PurchaseHistoryAPIView


urlpatterns = [
    path('', ProductAPIView.as_view(), name='api-product'),
    path('history/', PurchaseHistoryAPIView.as_view(), name='purchase-history'),
    path('product/<str:pk>/', ProductDetailAPIView.as_view(), name='api-product-details'),
]