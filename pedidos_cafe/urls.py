# Django imports
from django.contrib import admin
from django.urls import path, include

# Rest framework imports
from rest_framework import routers

# Local imports
from pedidos_cafe.views import PedidoCafeViewSet

# Create a router and register our viewset with it.
router = routers.DefaultRouter()

router.register(r"pedidos_cafe", PedidoCafeViewSet, basename="pedidos_cafe")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]