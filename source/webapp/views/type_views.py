from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import TypeForm
from webapp.models import Type
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView


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
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type_view', kwargs={'pk': self.object.pk})


class TypeUpdateView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data={
            'type_name': type.type_name,
            })
        return render(request, 'types/type_update.html', context={'form': form, 'type': type})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            type.type_name = data['type_name']
            type.save()
            return redirect('type_view', pk=type.pk)
        else:
            return render(request, 'types/type_update.html', context={'form': form, 'type': type})


class TypeDeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        return render(request, 'types/type_delete.html', context={'type': type})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        type.delete()