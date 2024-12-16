import pytz
from datacenter.models import Visit, get_duration
from django.shortcuts import render
from django.conf import settings


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visit in visits:
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at.astimezone(pytz.timezone(settings.TIME_ZONE)),
            'duration': get_duration(visit)
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
