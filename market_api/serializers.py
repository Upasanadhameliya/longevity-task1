from base.serializers import ModelSerializer
from .models import MarketApi

class MarketApiSerializers(ModelSerializer):

    class Meta:
        model = MarketApi
        read_only_fields = ("id","created_date_time","updated_date_time",)
