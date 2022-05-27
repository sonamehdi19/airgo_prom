"""airgoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from sender_jobs import views as jobs_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from users.views import (
    RegisterView,
    logout_view
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs_views.home, name="home_page"),
    path('join/', RegisterView.as_view(), name="join_page"),
    path('senders/', jobs_views.SenderJobListView.as_view(), name="senders_page"),
    path('carriers/', jobs_views.CarrierJobListView.as_view(), name="carriers_page"),
    path('account/', jobs_views.account, name="account_page"),
    path('logout/', logout_view, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
