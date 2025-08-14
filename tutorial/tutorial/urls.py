"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# try and error
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quickstart import views
from django.views.generic import TemplateView  # Add this import
from django.views.generic.base import RedirectView  # Import RedirectView


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'cart', views.CartViewSet, basename='cart')
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'payments', views.PaymentViewSet, basename='payment')
router.register(r'feedback', views.FeedbackViewSet, basename='feedback')

urlpatterns = [
     # Root URL redirects to API
    path('', RedirectView.as_view(url='/api/v1/')),  # Add this line
    
    # Admin URL
    path('admin/', admin.site.urls),
    
    # API URLs
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
