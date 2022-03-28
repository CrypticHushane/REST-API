from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'league', views.LeagueViewSet)
router.register(r'clubs', views.FootballClubViewSet)

urlpatterns = [
    path(r'',include(router.urls))
]