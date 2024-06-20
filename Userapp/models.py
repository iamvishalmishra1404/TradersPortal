from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
# In models.py


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=50)
    scripcode = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'company')

class Price(models.Model):
    id = models.IntegerField(primary_key=True)
    price = models.FloatField(null=True,blank=True)
    open = models.FloatField(null=True,blank=True)
    high = models.FloatField(null=True,blank=True)
    low = models.FloatField(null=True,blank=True)
    volume = models.IntegerField(null=True,blank=True)
    price_diff = models.FloatField(null=True,blank=True)
    change =   models.FloatField(null=True,blank=True)
    date = models.DateTimeField(default=str(timezone.now))
    company_id= models.IntegerField(null=True,blank=True)
    symbol = models.CharField(max_length=50)
