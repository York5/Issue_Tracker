from django.urls import reverse, reverse_lazy
from webapp.forms import IssueForm
from webapp.models import Issue
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
    template_name = 'issues/update.html'
    form_class = IssueForm
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issues/delete.html'
    context_object_name = 'issue'
    success_url = reverse_lazy('index')


