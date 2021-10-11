from base.admin import BaseAdmin
from .models import *
from django.contrib import admin

# Register your models here.
@admin.register(LongevityParams)
class LongevityParamsAdmin(BaseAdmin):
    pass

@admin.register(WelltoryParams)
class WelltoryParamsAdmin(BaseAdmin):
    pass

@admin.register(WelltorySubscription)
class WelltorySubscriptionAdmin(BaseAdmin):
    pass

@admin.register(LongevitySubscription)
class LongevitySubscriptionAdmin(BaseAdmin):
    pass


