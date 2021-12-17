"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from order.views import CreateOrderView, UserOrderList, UpdateOrderStatusView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('account.urls')),
    path('api/v1/', include('product.urls')),
    path('api/v1/orders/', CreateOrderView.as_view()),
    path('api/v1/order/own/', UserOrderList.as_view()),
    path('api/v1/orders/<int:pk>/', UpdateOrderStatusView.as_view())
]

if settings.DEBUG:
    urlpatterns += static('settings.MEDIA.URL, document_root=settings.MEDIA.ROOT')
    # path('api/v1/products/', ProductViewSet.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('api/v1/products/<int:pk>/', ProductViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update',
    #      'patch': 'partial_update', 'delete': 'destroy'}
    # ))