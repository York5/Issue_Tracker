from datetime import timedelta, datetime

from webapp.models import Issue, Project, Status, Type
from django.db.models import Q

qs_1 = Issue.objects.filter(Q(status__status_name='Done')) & (Q(created_at__lte=datetime.today(), created_at__gt=datetime.today()-timedelta(days=30)))
print(qs_1)
qs_2 = Type.objects.filter()
print(qs_2)
qs_3 = Project.objects.filter(Q(issues__description__icontains=self.search_value))
print(qs_3)