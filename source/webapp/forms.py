from django import forms
from webapp.models import Status, Type, Issue


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