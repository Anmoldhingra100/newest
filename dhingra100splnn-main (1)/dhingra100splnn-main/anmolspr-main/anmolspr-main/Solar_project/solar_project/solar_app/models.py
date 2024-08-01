from django.db.models import Sum
from django.utils import timezone
from django.db.models.functions import TruncWeek
from django.db import models

class MySolarrr(models.Model):
    
    solar_generation = models.IntegerField(default=0)
    daily_production = models.IntegerField(default=0)
    monthly_sales = models.IntegerField(default=0)
    weekly_revenue = models.IntegerField(default=0)
    invertor_power_distribution = models.IntegerField(default=0)
    total_panels = models.IntegerField(default=0)
    performance = models.CharField(max_length=200, default='')
    weather_prediction = models.IntegerField(default=0)
    hourly_temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)

    def __str__(self):
        return f"Data for {self.id}"

    @classmethod
    def get_weekly_data(cls):
        today = timezone.now().date()
        start_of_week = today - timezone.timedelta(days=today.weekday())  # Monday of the current week
        
        weekly_data = cls.objects.filter(date__gte=start_of_week).annotate(
            week=TruncWeek('date')
        ).values(
            'week'
        ).annotate(
            total_solar_generation=Sum('solar_generation'),
            total_daily_production=Sum('daily_production'),
            total_monthly_sales=Sum('monthly_sales'),
            total_weekly_revenue=Sum('weekly_revenue'),
            total_invertor_power_distribution=Sum('invertor_power_distribution'),
            total_total_panels=Sum('total_panels'),
            total_weather_prediction=Sum('weather_prediction'),
            total_hourly_temperature=Sum('hourly_temperature'),
            total_humidity=Sum('humidity')
        ).order_by('week')
        
        return weekly_data
