from django.urls import path,include
from chatProject import settings
from django.conf.urls.static import static
from django.contrib import admin;

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("api/",include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

