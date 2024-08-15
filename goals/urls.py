from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .api.api_views import GoalAPIViewSet, TaskAPIViewSet

router = SimpleRouter()
router.register(r'goals', GoalAPIViewSet)
router.register(r'tasks', TaskAPIViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]