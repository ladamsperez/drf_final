# e1337/urls.py
from django.urls import include, path
from rest_framework import routers, viewsets
from e1337 import viewsets

app_name = 'e1337'

router = routers.DefaultRouter()
router.register(r'', viewsets.E1337ViewSet)

# Wire API using automatic URL routing.
# Include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]