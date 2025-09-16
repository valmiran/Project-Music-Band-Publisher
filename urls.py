from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),               # rota da home
    path('accounts/', include('accounts.urls')),
    path('publications/', include('publications.urls')),
    path('events/', include('events.urls')),
    path('projects/', include('projects.urls')),
    path('selections/', include('selections.urls')),
    path('media/', include('mediahub.urls')),
    path('partners/', include('partners.urls')),
    path('auth/', include('django.contrib.auth.urls')),  # login/logout
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
