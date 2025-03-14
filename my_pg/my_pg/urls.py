"""
URL configuration for my_pg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from auth.views import RegisterViewSet, LoginViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', RegisterViewSet.as_view(), name='register'),
    path('login/', LoginViewSet.as_view(), name='login'),

    path('api/', include('tenants.urls')),
    
    path('api/', include('rooms.urls')),

    path('api/', include('payments.urls')),

    path('api/', include('staffs.urls')),

    path('api/', include('complaints.urls')),

    path('api/', include('inventory.urls')),

    path('api/', include('facilities.urls')),
    
    path('api/', include('expenses.urls')),

    path('api/', include('notifications.urls')),

    path('api/', include('dashboard.urls')),

    path('api/', include('owners.urls')),
]
