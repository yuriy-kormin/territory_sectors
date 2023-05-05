"""territory_sectors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import IndexView, UserLoginView, UserLogoutView, UUIDView
from django.conf import settings
from django.conf.urls.static import static

# import shortuuid

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='root'),
    path('<str:pk>', UUIDView.as_view(), name='uuid'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('flat/', include('territory_sectors.flat.urls')),
    path('house/', include('territory_sectors.house.urls')),
    path('sector/', include('territory_sectors.sector.urls')),
    path('uuid/', include('territory_sectors.uuid_qr.urls')),
    path('issue/', include('territory_sectors.issue.urls')),
]
if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
