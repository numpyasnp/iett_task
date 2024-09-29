from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTAuthenticationMixin:
    authentication_classes = [JWTAuthentication]


class JWTIsAuthenticatedMixin(JWTAuthenticationMixin):
    permission_class = [IsAuthenticated]
