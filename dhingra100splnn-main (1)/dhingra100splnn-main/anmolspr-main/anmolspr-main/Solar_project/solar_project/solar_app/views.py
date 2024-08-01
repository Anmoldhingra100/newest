from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Sum
from django.db.models.functions import TruncWeek
from .models import MySolarrr
# Create your views here.


def home_page_view(request):
    return request(request,'solarr.html')

def solr(request):
    mysolr=mysolarrr()
    if request.method == "POST":
     
        # Retrieve form data
    
            total=request.POST['total']
            production=request.POST['production']
            bkk=request.POST['bkk']
            
        
            # Create a new user
       
        
            mysolr.total=total
            mysolr.production=production
            mysolr.bkk=bkk
            
      
            mysolr.save()
        
        

      

        # Handle other logic (e.g., activation email, redirect, etc.)

    # Render your registration template
       
    return HttpResponse(request,'htfile.html')







def weekly_data_view(request):
    today = timezone.now().date()
    start_of_week = today - timezone.timedelta(days=today.weekday())  # Monday of the current week

    weekly_data = MySolarrr.objects.filter(date__gte=start_of_week).annotate(
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
    
    context = {
        'weekly_data': weekly_data
    }
    
    return render(request, 'weekly_data.html', context)





    




