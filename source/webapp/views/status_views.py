from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import StatusForm
from webapp.models import Status
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class StatusIndexView(ListView):
    template_name = 'statuses/status_index.html'
    context_object_name = 'statuses'
    model = Status


class StatusView(DetailView):
    template_name = 'statuses/status.html'
    model = Status


class StatusCreateView(CreateView):
    model = Status
    template_name = 'statuses/status_create.html'
    fields = ['status_name']

    def get_success_url(self):
        return reverse('status_view', kwargs={'pk': self.object.pk})


class StatusUpdateView(UpdateView):
    model = Status
    fields = ['status_name']
    template_name = 'statuses/status_update.html'

    def get_success_url(self):
        return reverse('status_view', kwargs={'pk': self.object.pk})

class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        return render(request, 'statuses/status_delete.html', context={'status': status})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        status.delete()
        return redirect('status_index')