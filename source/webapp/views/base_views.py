from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import TemplateView


class UpdateView(View):
    fields = None
    template_name = None
    model = None
    redirect_url = None

    def get(self, request, *args, **kwargs):
        form = self.fields()
        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        form = self.fields(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_redirect_url(self):
        return self.redirect_url

    def form_valid(self, form):
        self.object = self.model.objects.create(**form.cleaned_data)
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})

#
# class DetailView(TemplateView):
#     context_key = 'object'
#     model = None
#     key_kwarg = 'pk'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context[self.context_key] = self.get_object()
#         return context
#
#     def get_object(self):
#         pk = self.kwargs.get(self.key_kwarg)
# return get_object_or_404(self.model, pk=pk)


class DeleteView(View):
    model = None
    key_kwarg = 'pk'
    template_name = None
    redirect_url = None
    context_key = 'object'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.object = get_object_or_404(self.model, pk=pk)
        return render(request, self.template_name, context={self.context_key: self.object})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.object = get_object_or_404(self.model, pk=pk)
        self.object.delete()
        return redirect(self.redirect_url())