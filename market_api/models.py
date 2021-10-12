from __future__ import unicode_literals

from base.models import BaseModel
from django.db import models
from account.models import User


class LongevityParams(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_pressure = models.BooleanField(null=True, blank=True, default=None)
    heart_rate_variablity = models.BooleanField(null=True, blank=True, default=None)
    heart_rate = models.BooleanField(null=True, blank=True, default=None)
    vo2max = models.BooleanField(null=True, blank=True, default=None)
    common_diseases = models.BooleanField(null=True, blank=True, default=None)
    prescribed_medicines = models.BooleanField(null=True, blank=True, default=None)
    movement_sleep = models.BooleanField(null=True, blank=True, default=None)
    libido = models.BooleanField(null=True, blank=True, default=None)
    body_temperature = models.BooleanField(null=True, blank=True, default=None)
    lung_function = models.BooleanField(null=True, blank=True, default=None)
    blood_glucose = models.BooleanField(null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "LongevityParams"


class WelltoryParams(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heart_rate_variablity = models.BooleanField(null=True, blank=True, default=None)
    vo2max = models.BooleanField(null=True, blank=True, default=None)
    prescribed_medicines = models.BooleanField(null=True, blank=True, default=None)
    body_temperature = models.BooleanField(null=True, blank=True, default=None)
    blood_glucose = models.BooleanField(null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "WelltoryParams"


class WelltorySubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email}"


class LongevitySubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email}"
