from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import RecommendationsViewSet, TrackerViewSet

app_name = 'api'

router = DefaultRouter()

router.register(
    'tracker',
    TrackerViewSet
)
router.register(
    r'tracker/(?P<user_id>\d+)/recommendations',
    RecommendationsViewSet,
    basename='tracker_recommendations'
)

schema_view = get_schema_view(
    openapi.Info(
        title="Development tracker API",
        default_version='v1',
        description="Документация для проекта Трекер развития",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.authtoken')),
    path(
        'v1/docs/swagger_tracker.yaml',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'v1/docs/swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'v1/docs/redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    )
]
