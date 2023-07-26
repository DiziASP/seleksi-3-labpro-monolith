from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

from .permissions import IsUserAuthenticated

# Create your views here.
class ProductAPIView(ListAPIView):
    permission_classes = (IsUserAuthenticated,)
    template_name = 'core/index.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)
    
    