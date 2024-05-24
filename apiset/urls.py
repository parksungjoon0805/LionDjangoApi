from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apiset.views import ProductViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'profile', ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

