from account.permission import BaseModelPermissions
from base.views import ModelViewSet
from .serializers import (
    MarketApiSerializers
)
from .models import MarketApi

class MarketApiViewSet(ModelViewSet):
    serializer_class = MarketApiSerializers
    permission_classes = (BaseModelPermissions,)
    queryset = MarketApi.objects.all()
