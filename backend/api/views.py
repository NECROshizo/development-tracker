from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from .serializers import UserCourseSerializer, UserLevelSerializer
from course.models import UserCourse, UserLevel


class TrackerViewSet(viewsets.ModelViewSet):
	"""Вьюсет трекера развития."""

	queryset = UserLevel.objects.all()
	serializer_class = UserLevelSerializer
	http_method_names = ["get", "patch"]

	@swagger_auto_schema(
		responses={200: UserLevelSerializer(many=True)},
		operation_summary="Список навыков пользователя",
		operation_description=("Выводит параметры профиля пользователя."),
	)
	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)

	@swagger_auto_schema(
		responses={200: UserLevelSerializer(many=True)},
		operation_summary="Редактирование парамеров пользователя",
		operation_description=("Позваляет отредактировать параметры: профессия и грейт"),
	)
	def partial_update(self, request, *args, **kwargs):
		return super().partial_update(request, *args, **kwargs)


class RecommendationsViewSet(viewsets.ModelViewSet):
	queryset = UserCourse.objects.all()
	serializer_class = UserCourseSerializer
	http_method_names = ["get"]

	@swagger_auto_schema(
		responses={200: UserCourseSerializer(many=True)},
		operation_summary="Список рекомендаций для пользователя",
		operation_description=("Выводит рекомендации для пользователя трекера."),
	)
	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)
