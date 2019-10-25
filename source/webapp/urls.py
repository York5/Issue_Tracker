from django.urls import path
from webapp.views import IndexView, IssueView, IssueCreateView, IssueUpdateView, IssueDeleteView, StatusIndexView,\
    StatusCreateView, StatusDeleteView, StatusUpdateView, StatusView, TypeIndexView, TypeCreateView, TypeDeleteView,\
    TypeUpdateView, TypeView, ProjectIndexView, ProjectView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issue/<int:pk>', IssueView.as_view(), name='issue_view'),
    path('issue/<int:pk>/update/', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),

    path('statuses', StatusIndexView.as_view(), name='status_index'),
    path('statuses/status/<int:pk>', StatusView.as_view(), name='status_view'),
    path('statuses/status/add/', StatusCreateView.as_view(), name='status_add'),
    path('statuses/status/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('statuses/status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),

    path('types', TypeIndexView.as_view(), name='type_index'),
    path('types/type/<int:pk>', TypeView.as_view(), name='type_view'),
    path('types/type/add/', TypeCreateView.as_view(), name='type_add'),
    path('types/type/<int:pk>/update/', TypeUpdateView.as_view(), name='type_update'),
    path('types/type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),

    path('projects', ProjectIndexView.as_view(), name='project_index'),
    path('projects/project/<int:pk>', ProjectView.as_view(), name='project_view'),
    path('projects/project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('projects/project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    ]

app_name = 'webapp'