# -*- coding: utf-8 -*-
""" Stores Abstract models for other apps"""

from django.db import models


class AbstractDTBaseModel(models.Model):
    """
    Abstract model class to register default fields to children models
    """
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        """
        Meta properties of ModelBase
        """
        abstract = True


class AbstractActiveModel(models.Model):
    """
    Abstract model to add is_active flag to children models
    """
    is_active = models.BooleanField(default=True)

    class Meta:
        """
        Meta properties of ModelBase
        """
        abstract = True