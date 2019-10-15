from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from webapp.forms import ProjectForm
from webapp.models import Project, STATUS_CHOICES
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProjectIndexView(ListView):
    template_name = 'projects/project_index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['-created_at']
    paginate_by = 6
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_project'] = self.model.objects.filter(status='active').order_by('created_at')
        context['closed_project'] = self.model.objects.filter(status='closed').order_by('created_at')
        return context


class ProjectView(DetailView):
    template_name = 'projects/project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        issues = project.issues.order_by('-created_at')
        paginator = Paginator(issues, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['issues'] = page.object_list
        context['is_paginated'] = page.has_other_pages()
        return context


class ProjectCreateView(CreateView):
    form_class = ProjectForm
    model = Project
    template_name = 'projects/project_create.html'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('project_index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.status = 'closed'
        self.object.save()
        return HttpResponseRedirect(success_url)
