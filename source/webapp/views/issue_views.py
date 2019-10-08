from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import IssueForm
from webapp.models import Issue
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView


class IndexView(ListView):
    template_name = 'issues/index.html'
    context_object_name = 'issues'
    model = Issue
    ordering = ['-created_at']
    paginate_by = 2
    paginate_orphans = 1


class IssueView(DetailView):
    template_name = 'issues/issue.html'
    model = Issue


class IssueCreateView(CreateView):
    form_class = IssueForm
    model = Issue
    template_name = 'issues/create.html'

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status_id,
            'type': issue.type_id,
            })
        return render(request, 'issues/update.html', context={'form': form, 'issue': issue})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            issue.summary = data['summary']
            issue.description = data['description']
            issue.status = data['status']
            issue.type = data['type']
            issue.save()
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'issues/update.html', context={'form': form, 'issue': issue})


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