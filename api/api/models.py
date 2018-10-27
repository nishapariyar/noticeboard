# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Noticelist(models.Model):
    title = models.TextField(max_length=100)
    notice_text = models.TextField(max_length=None)
    date_expiry = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__ (self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

