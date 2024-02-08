from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RecommendationsViewSet, TrackerViewSet

router = DefaultRouter()

router.register("tracker", TrackerViewSet)
router.register(r"tracker/(?P<user_id>\d+)/recommendations", RecommendationsViewSet, basename="tracker_recommendations")

urlpatterns = [
	path("v1/", include(router.urls)),
	path("v1/", include("djoser.urls")),
	path("v1/auth/", include("djoser.urls.authtoken")),
	path("v1/schema/", SpectacularAPIView.as_view(), name="schema"),
	path("v1/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
