from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('investimentos.urls')),  # Inclui as rotas da API
]
