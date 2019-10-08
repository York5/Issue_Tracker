from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import IssueForm
from webapp.models import Issue
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from webapp.views.base_views import DeleteView, UpdateView


class IndexView(ListView):
    template_name = 'issues/index.html'
    context_object_name = 'issues'
    model = Issue
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1


class IssueView(DetailView):
    template_name = 'issues/issue.html'
    model = Issue


class IssueCreateView(CreateView):
    model = Issue
    template_name = 'issues/create.html'
    fields = ['summary', 'description', 'status', 'type']

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(UpdateView):
    model = Issue
    fields = ['summary', 'description', 'status', 'type']
    template_name = 'issues/update.html'

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issues/delete.html'
    confirm = True

    def get_success_url(self):
        return reverse('index')


