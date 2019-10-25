from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from webapp.forms import TypeForm
from webapp.models import Type
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class TypeIndexView(ListView):
    template_name = 'types/type_index.html'
    context_object_name = 'types'
    model = Type


class TypeView(DetailView):
    template_name = 'types/type.html'
    model = Type


class TypeCreateView(LoginRequiredMixin, CreateView):
    form_class = TypeForm
    model = Type
    template_name = 'types/type_create.html'

    def get_success_url(self):
        return reverse('webapp:type_view', kwargs={'pk': self.object.pk})


class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Type
    template_name = 'types/type_update.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('webapp:type_view', kwargs={'pk': self.object.pk})


class TypeDeleteView(LoginRequiredMixin, DeleteView):
    model = Type
    template_name = 'types/type_delete.html'
    context_object_name = 'type'
    success_url = reverse_lazy('webapp:type_index')

