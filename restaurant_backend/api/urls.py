from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FoodCategoryViewSet

v1_router = DefaultRouter()

v1_router.register(r'foods', FoodCategoryViewSet, basename='food')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
