from account.permission import BaseModelPermissions
from base.views import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .utils import random_bool_fields
from .serializers import *


class GetRisks(APIView):
    permission_classes = (IsAuthenticated,)
    risk_data = dict()
    serializer = None

    def generate_risks(self, request):
        if (
            request.user.is_subscribed_to_longevity()
            and request.user.is_subscribed_to_welltory()
        ):
            self.risk_data["longevity"] = random_bool_fields(LongevityParams)
            self.risk_data.update(
                random_bool_fields(WelltoryParams)
            )
        elif request.user.is_subscribed_to_longevity():
            self.risk_data.update(
                random_bool_fields(LongevityParams)
            )
            self.serializer = LongevitySerializer
        elif request.user.is_subscribed_to_welltory():
            self.risk_data.update(
                random_bool_fields(WelltoryParams)
            )

    def get(self, request):
        self.generate_risks(request)
        if self.risk_data:
            self.risk_data.update({"user":request.user.pk})
            self.serializer = self.serializer(data=self.risk_data)
            if self.serializer.is_valid():
                obj = self.serializer.save()
        return Response({"success": 200})
