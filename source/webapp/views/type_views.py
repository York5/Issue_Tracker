from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import TypeForm
from webapp.models import Type
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView


class TypeIndexView(ListView):
    template_name = 'types/type_index.html'
    context_object_name = 'types'
    model = Type


class TypeView(DetailView):
    template_name = 'types/type.html'
    model = Type


class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = TypeForm()
            return render(request, 'types/type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(
                type_name=form.cleaned_data['type_name'],
                )
            return redirect('type_view', pk=type.pk)
        else:
            return render(request, 'types/type_create.html', context={'form': form})


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