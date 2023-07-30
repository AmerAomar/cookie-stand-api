import random
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class CookieStand(models.Model):
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
    total = models.IntegerField(default=0)  # New field for storing the sum of hourly sales

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse("cookie_stands:cookie_stand_detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.hourly_sales:
            self.hourly_sales = self.generate_random_hourly_sales()
        self.total = sum(self.hourly_sales)  # Calculate the total from hourly_sales
        super(CookieStand, self).save(*args, **kwargs)

    def generate_random_hourly_sales(self):
        hourly_sales_values = [48, 42, 30, 24, 42, 24, 36, 42, 42, 48, 36, 42, 24, 36]
        return random.choices(hourly_sales_values, k=14)  # 14 hours from 6 am until 7 pm
