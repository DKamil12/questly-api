from django.urls import path, include
from .api.api_views import TaskCompletionAPIViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'task-completions', TaskCompletionAPIViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]