from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
from web.rental.models import Address
from web.users.constant import Gender,Type


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='user_address', null=False)
    active=models.BooleanField(null=False,default=True)
    Type=models.IntegerField(choices=Type.FieldStr.items(),default=Type.customer,null=False)
    bio = models.TextField(null=True)
    gender = models.IntegerField(choices=Gender.FieldStr.items(), default=Gender.male, null=False)
    created_ts = models.DateTimeField(_("Created Date"), auto_now_add=True)
    updated_ts = models.DateTimeField(_("Last Updated Date"), auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "users_profile"
        verbose_name_plural = "User Profile"


