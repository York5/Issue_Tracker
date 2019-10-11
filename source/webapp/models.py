from django.db import models

ACTIVE = 'active'
STATUS_CHOICES = [(ACTIVE, 'Active'), ('closed', 'Closed')]


class Project(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Project Name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Time Updated')
    status = models.CharField(max_length=40, null=False, blank=False, verbose_name='Status', default=ACTIVE,
                              choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class Issue(models.Model):
    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, null=False, blank=False, verbose_name='Status',
                               related_name='issues')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, null=False, blank=False, verbose_name='Type',
                             related_name='issues')
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=True, blank=False, verbose_name='Project',
                                related_name='issues')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time Created')

    def __str__(self):
        return self.summary


class Status(models.Model):
    status_name = models.CharField(max_length=20, verbose_name='Name')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Type(models.Model):
    type_name = models.CharField(max_length=20, verbose_name='Name')

    def __str__(self):
        return self.type_name

