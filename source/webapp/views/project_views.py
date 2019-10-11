from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from webapp.forms import ProjectForm
from webapp.models import Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProjectIndexView(ListView):
    template_name = 'projects/project_index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1


class ProjectView(DetailView):
    template_name = 'projects/project.html'
    model = Project


class ProjectCreateView(CreateView):
    form_class = Project
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
    context_object_name = 'project'
    success_url = reverse_lazy('project_index')
