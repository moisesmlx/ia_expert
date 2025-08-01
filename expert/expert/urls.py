
from django.contrib import admin
from django.urls import path, include
from expert_em_cifras import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('expert_em_cifras.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
