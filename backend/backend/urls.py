from django.contrib import admin
from django.urls import path
from e1337 import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/e1337', views.e1337_list),
    path('api/e1337/<int:pk>/', views.e1337_detail),
    path('api/e1337/published', views.e1337_list_published)
]
