from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import IssueForm
from webapp.models import Issue, Status, Type
from django.http import Http404


def index_issues_view(request, *args, **kwargs):
    issues = Issue.objects.all()
    return render(request, 'index.html', context={
        'issues': issues,
    })


def single_issue_view(request, pk):
    try:
        issue = get_object_or_404(Issue, pk=pk)
    except Issue.DoesNotExist:
        raise Http404
    return render(request, 'issue.html', context={
        'issue': issue
    })


def issue_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = IssueForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_date['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type'],
                created_at=form.cleaned_data['created_at'])
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def issue_update_view(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'GET':
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status_id,
            'type': issue.type_id,
            'created_at': issue.created_at
            })
        return render(request, 'update.html', context={'form': form, 'issue': issue})
    elif request.method == 'POST':
        form = IssueForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            issue.description = data['description']
            issue.status = data['status']
            issue.type = data['type']
            issue.created_at = data['created_at']
            issue.save()
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'issue': issue})


def issue_delete_view(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'issue': issue})
    elif request.method == 'POST':
        issue.delete()
        return redirect('index')
