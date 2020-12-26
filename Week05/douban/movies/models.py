from django.db import models

class Comments(models.Model):
    cid = models.IntegerField(primary_key=True)
    updatetime = models.DateTimeField(null=True)
    username = models.CharField(max_length=30)
    star = models.PositiveSmallIntegerField(null=True)
    short = models.TextField(null=True)
