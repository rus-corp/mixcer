from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TarifViewSet, TarifChoiceViewSet




router = DefaultRouter()

router.register('all', TarifViewSet)
router.register('create', TarifChoiceViewSet)





urlpatterns = [
    path('', include(router.urls))
]