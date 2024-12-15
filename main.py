import os
import django
from django.utils.timezone import activate
import pytz
from django.core.management import execute_from_command_line
from project.settings import TIME_ZONE


TIME_ZONE = pytz.timezone(TIME_ZONE)


def get_duration(visit):
    if visit.leaved_at == None:
        return (django.utils.timezone.localtime() - visit.entered_at.astimezone(TIME_ZONE))
    return (visit.leaved_at - visit.entered_at)


def is_visit_long(visit, minutes=60):
    timedelta = get_duration(visit)
    if timedelta.total_seconds() >= minutes*60:
        return True
    return False


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    execute_from_command_line('manage.py runserver 127.0.0.1:8000'.split())


if __name__ == '__main__':
    main()
