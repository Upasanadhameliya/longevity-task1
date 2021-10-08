from base.admin import BaseAdmin
from .models import MarketApi

# Register your models here.
@admin.register(MarketApi)
class MarketApiAdmin(BaseAdmin):
    pass