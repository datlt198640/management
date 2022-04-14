from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(unique=True, max_length=128, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=128, null=True, blank=True)

    token_context = models.CharField(max_length=256, blank=True, default="")
    token_signature = models.CharField(max_length=128, blank=True, default="")
    token_refresh_limit = models.DateTimeField(null=True, blank=True, default=None)

    def clean(self) -> None:
        username_arr = []
        if not self.phone_number:
            self.phone_number = None
        else:
            username_arr.append(self.phone_number)

        if not self.email:
            self.email = None
        else:
            username_arr.append(self.email)

        if not self.phone_number and not self.email:
            raise ValidationError(
                [_("Email and phone number can not be blank together")],
                code="phone_number",
            )

        self.username = "-".join(username_arr)

    def save(self, *arg, **kwarg):
        self.clean()
        super().save(*arg, **kwarg)

    class Meta:
        db_table = "users"
        ordering = ["-id"]
        verbose_name = _("user")