from django.urls import reverse, reverse_lazy
from webapp.forms import StatusForm
from webapp.models import Status
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class StatusIndexView(ListView):
    template_name = 'statuses/status_index.html'
    context_object_name = 'statuses'
    model = Status


class StatusView(DetailView):
    template_name = 'statuses/status.html'
    model = Status


class StatusCreateView(CreateView):
    form_class = StatusForm
    model = Status
    template_name = 'statuses/status_create.html'

    def get_success_url(self):
        return reverse('status_view', kwargs={'pk': self.object.pk})


class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'statuses/status_update.html'
    form_class = StatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status_view', kwargs={'pk': self.object.pk})


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'statuses/status_delete.html'
    context_object_name = 'status'
    success_url = reverse_lazy('status_index')