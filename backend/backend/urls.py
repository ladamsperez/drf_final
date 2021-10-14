from django.contrib import admin
from django.urls import path, include
from e1337 import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('e1337.urls')),
]
