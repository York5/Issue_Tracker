from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import IssueForm
from webapp.models import Issue
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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


class IssueDeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        return render(request, 'issues/delete.html', context={'issue': issue})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('index')


class IssueDelete(DeleteView):
    model = Issue
    template_name = 'issues/delete.html'

    def get_success_url(self):
        return reverse('index')


