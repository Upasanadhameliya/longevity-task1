"""Add all API routes."""
from rest_framework import routers

from django.urls import path, include

from . import views


router = routers.DefaultRouter(trailing_slash=False)

# router.register(r'', MarketApiViewSet, basename='market_api')


urlpatterns = [
    # path('', include(router.urls)),
    path('getrisks/',views.GetRisks.as_view(),name='getrisks')
]
