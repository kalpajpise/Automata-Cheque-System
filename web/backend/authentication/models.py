from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import AbstractActiveModel, AbstractDTBaseModel


# Create your models here.

class User(AbstractUser, AbstractDTBaseModel):
    """
    User model created here
    """
    name = models.CharField(max_length=128, null=False, blank=False)
    contact_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=128, blank=False, unique=True, null=False)

    def __str__(self):
        return "%s" % (self.name)
