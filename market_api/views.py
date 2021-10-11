from account.permission import BaseModelPermissions
from base.views import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# from .serializers import (
#     MarketApiSerializers
# )
from rest_framework.decorators import permission_classes
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class GetRisks(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        return Response({"success":200})
