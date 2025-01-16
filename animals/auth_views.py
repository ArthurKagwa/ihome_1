from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from animals.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    # You can customize the serializer if needed
    serializer_class = MyTokenObtainPairSerializer
class MyTokenRefreshView(TokenRefreshView):
    # You can customize the serializer if needed
    pass