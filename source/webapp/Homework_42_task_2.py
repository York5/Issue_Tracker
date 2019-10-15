from datetime import timedelta, datetime

from webapp.models import Issue, Project, Status, Type
from django.db.models import Q

qs_1 = Issue.objects.filter(Q(status__status_name='Done') & Q(created_at__lte=datetime.today(), created_at__gte=datetime.today()-timedelta(days=30)))
print(qs_1)
qs_2 = Issue.objects.filter(project__name='Moon Gateway').values('type__type_name','project__name')
print(qs_2)
qs_3 = Issue.objects.filter(Q(project__description__icontains='new'))
print(qs_3)