from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cats.views import CatViewSet


router = SimpleRouter()
router.register('cats', CatViewSet)
urlpatterns = [
   path('', include(router.urls)),
]
