from django.contrib import admin
from .models import MySolarrr

class solarAdmin(admin.ModelAdmin):
    list_display = ['solar_generation','daily_production','monthly_sales','weekly_revenue','invertor_power_distribution','hourly_temperature','total_panels','performance','weather_prediction','hourly_temperature','humidity']  # Fields to display in the list view
     # Fields to display in the list view
   

admin.site.register(MySolarrr, solarAdmin)





