from rest_framework import viewsets

from rest_framework import viewsets
from .permissions import IsAdminOrOwner
from django.contrib.auth.models import E1337

from e1337 import E1337Serializer


class E1337ViewSet(viewsets.ModelViewSet):
    queryset = E1337.objects.all()
    serializer_class = E1337Serializer
    # lookup_field = 'username'
    # permission_classes = [IsAdminOrOwner]

