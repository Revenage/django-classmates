from django.shortcuts import render
from .models import SheduleItem, DAYS_OF_WEEK

# Create your views here.
def schedule(request):
    db_schedules = SheduleItem.objects.order_by('day')
    normalize_days = (day[1] for day in DAYS_OF_WEEK)
    schedules = [];
    for day_num, day_name in DAYS_OF_WEEK:
        res = {day_name: SheduleItem.objects.filter(day=day_num)}
        schedules.append(res)

    return render(request, 'schedule/index.html', {'schedules': schedules, 'days': normalize_days})