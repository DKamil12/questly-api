from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .api.api_views import CharacterAPIViewSet

router = SimpleRouter()
router.register(r'characters', CharacterAPIViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]