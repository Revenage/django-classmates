from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from .models import SheduleItem, DAYS_OF_WEEK

class ScheduleView (ListView):
    model = SheduleItem
    template_name = 'schedule/index.html'
    context_object_name = 'schedules'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ScheduleView, self).dispatch(*args, **kwargs)

# Create your views here.
# def schedule(request):
#     db_schedules = SheduleItem.objects.order_by('day')
#     normalize_days = (day[1] for day in DAYS_OF_WEEK)
#     schedules = [];
#     for day_num, day_name in DAYS_OF_WEEK:
#         res = {day_name: SheduleItem.objects.filter(day=day_num)}
#         schedules.append(res)

    # return render(request, 'schedule/index.html', {'schedules': schedules, 'days': normalize_days})