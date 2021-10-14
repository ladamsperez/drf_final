from rest_framework import viewsets
from .serializers import E1337Serializer
from .models import E1337

class E1337ViewSet(viewsets.ModelViewSet):
    queryset = E1337.objects.all().order_by('title')
    serializer_class = E1337Serializer