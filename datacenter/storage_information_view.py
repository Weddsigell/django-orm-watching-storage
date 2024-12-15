from datacenter.models import Visit
from django.shortcuts import render
from main import get_duration, TIME_ZONE


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visit in visits:
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at.astimezone(TIME_ZONE),
            'duration': get_duration(visit)
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
