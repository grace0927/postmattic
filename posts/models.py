from django.db import models


class NavItem(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=300)
