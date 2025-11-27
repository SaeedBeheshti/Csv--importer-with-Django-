from rest_framework.routers import DefaultRouter
from .views import ImportJobViewSet

router = DefaultRouter()
router.register(r'imports', ImportJobViewSet, basename='importjob')

urlpatterns = router.urls


