from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class MyTokenObtainPairView(TokenObtainPairView):
    # You can customize the serializer if needed
    pass

class MyTokenRefreshView(TokenRefreshView):
    # You can customize the serializer if needed
    pass