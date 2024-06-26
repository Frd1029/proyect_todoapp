from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

from .serializers import ProfileCreationSerializer

# Create your views here.


class ProfileCreationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ProfileCreationSerializer
    permission_classes = [AllowAny]
