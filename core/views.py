from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from django.contrib import messages

from .forms import UploadImageForm
from .models import GaleryPhoto


class GaleryView(ListView):
    """View that show up all data inputed"""
    model = GaleryPhoto
    paginate_by = 10
    template_name = 'galery.html'

    def get_context_data(self, **kwargs):
        context = super(GaleryView, self).get_context_data(**kwargs)
        context['photos'] = GaleryPhoto.objects.filter(approved=True)
        return context


class UploadImageCreateView(CreateView):
    """Uploading a specific image"""
    model = GaleryPhoto
    form_class = UploadImageForm
    template_name = "send_image.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # Verify form is valid
        if form.is_valid():
            # Call parent form_valid to create model record object
            super(UploadImageCreateView,self).form_valid(form)
            # Add custom success message   
            messages.success(self.request, "Imagem adicionada com sucesso!")
            return HttpResponseRedirect(self.get_success_url())
        # Form is invalid
        # Set object to None, since class-based view expects model record object
        self.object = None
        messages.error(self.request, f"Ops... você precisa adicionar uma foto. ")
        # Return class-based view form_invalid to generate form with errors
        return self.form_invalid(form)

    def get_success_url(self, *args):
        return reverse('core:upload_image')







