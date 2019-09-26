from django.db import models


class Issue(models.Model):
    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, null=False, blank=False, verbose_name='Status',
                               related_name='issues')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, null=False, blank=False, verbose_name='Status',
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