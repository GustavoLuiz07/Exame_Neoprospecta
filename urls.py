from django.contrib import admin
from django.urls import include, path
from pseletivo.views import Backend_DeveloperViewSet, Frontend_DeveloperViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'selection_process - approved_candidates - back-end', Backend_DeveloperViewSet)
router.register(r'selection_processf - approved_candidates - front-end', Frontend_DeveloperViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
