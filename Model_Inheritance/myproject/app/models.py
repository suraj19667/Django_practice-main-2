from django.db import models

# Create your models here.
class MainModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()

class ProxyModel(MainModel):
    class Meta:
        proxy=True