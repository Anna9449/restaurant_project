from django.db.models import Prefetch
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, viewsets

from .serializers import FoodListSerializer
from foods.models import Food, FoodCategory


@extend_schema_view(
    list=extend_schema(
        summary='api/v1/foods/ получение списка категорий блюд',
        description='Получение списка категорий блюд.',
    ),
)
class FoodCategoryViewSet(mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    """Вьюсет вывода списка категорий блюд."""

    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = FoodCategory.objects.prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        )
        return (queryset.filter(food__is_publish=True)
                .prefetch_related('food__additional'))
