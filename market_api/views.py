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
    slzr_data_map = dict()
    response = list()

    def generate_risks(self, request):

        if request.user.is_subscribed_to_longevity():
            self.slzr_data_map["longevity"] = [
                LongevitySerializer,
                random_bool_fields(LongevityParams),
            ]
        if request.user.is_subscribed_to_welltory():
            self.slzr_data_map["welltory"] = [
                WelltorySerializer,
                random_bool_fields(WelltoryParams),
            ]

    def get(self, request):
        self.generate_risks(request)

        if self.slzr_data_map:
            for key, (serializer, value) in self.slzr_data_map.items():
                value.update({"user": request.user.pk})
                serializer = serializer(data=value)
                if serializer.is_valid():
                    obj = serializer.save()
                    self.response.append({key: serializer.data})
        else:
            return Response({"User not subscribed": 400})

        return Response({"success": self.response})
