from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import StatusForm
from webapp.models import Status
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView


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
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_view', kwargs={'pk': self.object.pk})


class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data={
            'status_name': status.status_name,
            })
        return render(request, 'statuses/status_update.html', context={'form': form, 'status': status})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            status.status_name = data['status_name']
            status.save()
            return redirect('status_view', pk=status.pk)
        else:
            return render(request, 'statuses/status_update.html', context={'form': form, 'status': status})


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