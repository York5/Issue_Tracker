from django import forms
from webapp.models import Status, Type, Issue, Project


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['created_at']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status_name']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type_name']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Search')
