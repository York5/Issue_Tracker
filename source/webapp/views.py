from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import IssueForm, StatusForm, TypeForm
from webapp.models import Issue, Status, Type
from django.http import Http404
from django.views import View
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=pk)
        return context


class IssueCreateView(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = IssueForm()
            return render(request, 'create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type'],
                )
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'create.html', context={'form': form})


class IssueUpdateView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status_id,
            'type': issue.type_id,
            })
        return render(request, 'update.html', context={'form': form, 'issue': issue})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            issue.summary = data['summary']
            issue.description = data['description']
            issue.status = data['status']
            issue.type = data['type']
            issue.save()
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'issue': issue})


class IssueDeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        return render(request, 'delete.html', context={'issue': issue})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('index')


class StatusIndexView(TemplateView):
    template_name = 'status_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class StatusView(TemplateView):
    template_name = 'status.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['status'] = get_object_or_404(Status, pk=pk)
        return context


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = StatusForm()
            return render(request, 'status_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(
                status_name=form.cleaned_data['status_name'],
                )
            return redirect('status_view', pk=status.pk)
        else:
            return render(request, 'status_create.html', context={'form': form})


class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data={
            'status_name': status.status_name,
            })
        return render(request, 'status_update.html', context={'form': form, 'status': status})

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
            return render(request, 'status_update.html', context={'form': form, 'status': status})


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        return render(request, 'status_delete.html', context={'status': status})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        status.delete()
        return redirect('status_index')




class TypeIndexView(TemplateView):
    template_name = 'type_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeView(TemplateView):
    template_name = 'type.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['type'] = get_object_or_404(Type, pk=pk)
        return context


class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = TypeForm()
            return render(request, 'type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(
                type_name=form.cleaned_data['type_name'],
                )
            return redirect('type_view', pk=type.pk)
        else:
            return render(request, 'type_create.html', context={'form': form})


class TypeUpdateView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data={
            'type_name': type.type_name,
            })
        return render(request, 'type_update.html', context={'form': form, 'type': type})

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
            return render(request, 'type_update.html', context={'form': form, 'type': type})


class TypeDeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        return render(request, 'type_delete.html', context={'type': type})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        type.delete()
