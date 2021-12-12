from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from measurements import api_views

router = DefaultRouter()
router.register('project', api_views.ProjectViewSet)
router.register('measurements', api_views.MeasurementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
