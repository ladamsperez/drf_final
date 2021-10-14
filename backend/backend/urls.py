from django.contrib import admin
from django.urls import path, include
from e1337 import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('e1337.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
