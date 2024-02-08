from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from .serializers import UserCourseSerializer, UserLevelSerializer
from course.models import UserCourse, UserLevel


@extend_schema_view(
	list=extend_schema(
		summary="Список навыков",
		description="Выводит параметры профиля пользователя.",
		responses={200: UserLevelSerializer(many=True)},
		tags=("Tracker",),
	),
	retrieve=extend_schema(
		summary="Навыки конкретного пользователя",
		description="Позволяет отобразить список навыков для пользователя трека",
		responses={200: UserLevelSerializer()},
		tags=("Tracker",),
	),
	partial_update=extend_schema(
		summary="Редактирование парамеров пользователя",
		description="Позваляет отредактировать параметры: профессия и грейт.",
		responses={200: UserLevelSerializer(many=True)},
		tags=("Tracker",),
	),
)
class TrackerViewSet(viewsets.ModelViewSet):
	"""Вьюсет трекера развития."""

	queryset = UserLevel.objects.all()
	serializer_class = UserLevelSerializer
	http_method_names = ["get", "patch"]


@extend_schema_view(
	list=extend_schema(
		summary="Список рекомендаций для пользователя.",
		description="Выводит список рекомендаций для пользователя трека.",
		responses={200: UserCourseSerializer(many=True)},
		tags=("Tracker",),
	),
	retrieve=extend_schema(
		summary="Рекомендованный навык конкретного пользователя.",
		description="Позволяет отобразить список навыков для конкретного пользователя трека.",
		responses={200: UserLevelSerializer()},
		tags=("Tracker",),
	),
)
class RecommendationsViewSet(viewsets.ModelViewSet):
	queryset = UserCourse.objects.all()
	serializer_class = UserCourseSerializer
	http_method_names = ["get"]
