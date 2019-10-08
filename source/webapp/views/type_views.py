from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import TypeForm
from webapp.models import Type
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class TypeIndexView(ListView):
    template_name = 'types/type_index.html'
    context_object_name = 'types'
    model = Type


class TypeView(DetailView):
    template_name = 'types/type.html'
    model = Type


class TypeCreateView(CreateView):
    model = Type
    template_name = 'types/type_create.html'
    fields = ['type_name']

    def get_success_url(self):
        return reverse('type_view', kwargs={'pk': self.object.pk})


class TypeUpdateView(UpdateView):
    model = Type
    fields = ['type_name']
    template_name = 'types/type_update.html'

    def get_success_url(self):
        return reverse('type_view', kwargs={'pk': self.object.pk})


class TypeDeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        return render(request, 'types/type_delete.html', context={'type': type})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        type.delete()
        return redirect('type_index')
