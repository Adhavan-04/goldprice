from django.db import models

# Create your models here.
class GoldPrice(models.Model):
    SPX=models.FloatField()
    USO=models.FloatField()
    SLV=models.FloatField()
    EUR_USD=models.FloatField()
    GOLD=models.FloatField()