from rest_framework.permissions import BasePermission


class IsUserAuthenticated(BasePermission):

    message = 'You are unauthorized to perform any action.'

    def has_permission(self, request, view):
        AUTH_COOKIE = request.COOKIES.get('AUTH_COOKIE')
        if AUTH_COOKIE:
            return True
        return False