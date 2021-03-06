from datetime import timedelta, datetime
from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import IssueForm, SimpleSearchForm
from webapp.models import Issue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    template_name = 'issues/index.html'
    context_object_name = 'issues'
    model = Issue
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = SimpleSearchForm(data=self.request.GET)
        self.search = None
        if self.form.is_valid():
            self.search_value = self.form.cleaned_data['search']
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_value)
                | Q(description__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_search_form(self):
        return SimpleSearchForm(data=self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleanned_data['search']
        return None


class IssueView(DetailView):
    template_name = 'issues/issue.html'
    model = Issue


class IssueCreateView(CreateView):
    form_class = IssueForm
    model = Issue
    template_name = 'issues/create.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('accounts:login')

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    template_name = 'issues/update.html'
    form_class = IssueForm
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = 'issues/delete.html'
    context_object_name = 'issue'
    success_url = reverse_lazy('webapp:index')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


