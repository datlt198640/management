import os
import uuid
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models
from services.models.timestamped_model import TimeStampedModel
from services.models.consts import GENDER_CHOICES


def img_dest(instance, filename):
    ext = filename.split(".")[-1]
    return os.path.join("staff", f"{uuid.uuid4()}.{ext}")

class Staff(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=img_dest, null=True, blank=True)
    full_name = models.CharField(max_length=128)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    dob = models.DateField(null=True, default = None, blank=True)
    address = models.CharField(max_length= 225, null=True, blank=True)

    class Meta:
        db_table = "staffs"
        ordering = ["-id"]
        verbose_name = _("staff")