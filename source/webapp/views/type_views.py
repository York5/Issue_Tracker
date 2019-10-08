from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import TypeForm
from webapp.models import Type
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from webapp.views.base_views import DeleteView, UpdateView


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


class TypeDeleteView(DeleteView):
    context_key = 'type'
    model = Type
    confirm = True
    template_name = 'types/type_delete.html'
    redirect_url = '/types'

