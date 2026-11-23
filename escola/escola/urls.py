from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('',include('alunos.urls')),
    path('',include('professor.urls')),
    path('admin/', admin.site.urls),
]
