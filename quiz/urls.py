from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('task1/', include('task1.urls')),
    path('task2/', include('task2.urls')),
    path('task3/', include('task3.urls')),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.AUDIO_URL, document_root=settings.AUDIO_ROOT)
urlpatterns += static(settings.CSV_URL, document_root=settings.CSV_ROOT)
