from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse

from .serializers import RegisterSerializer, LoginSerializer

def get_tokens_for_user(user):
    access_token = AccessToken.for_user(user=user)
    print(user.username)
    return {
        'access': str(access_token),
        'username': user.username,
    }

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    template_name = 'auth/register.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response({})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        response = Response()
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return redirect(reverse('auth_login'))

        response.data = serializer.errors
        return redirect(reverse('auth_register'), response)

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    template_name = 'auth/login.html'
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request):
        if request.COOKIES.get('AUTH_COOKIE'):
            return redirect(reverse('api-product'))
        return Response({})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = User.objects.filter(username=serializer.validated_data['username']).first()
            token = get_tokens_for_user(user)
            response = redirect(reverse('api-product'))
            response.set_cookie(key='AUTH_COOKIE', value=token['access'], httponly=True)
            response.set_cookie(key='USERNAME', value=token['username'], httponly=True)
            return response
        
        messages.error(request, 'Username atau password salah')
        return redirect(reverse('auth_login'))
    

class LogoutView(APIView):
    def get(self, request):
        response = redirect(reverse('auth_login'))
        response.delete_cookie('AUTH_COOKIE')
        response.delete_cookie('USERNAME')
        return response