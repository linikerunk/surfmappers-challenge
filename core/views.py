from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, CreateView
from django.contrib import messages

from .forms import UploadImageForm, UploadImageManageForm
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
        print("ERRO : ", form.errors)
        messages.error(self.request, f"Ops... você precisa adicionar uma foto. ")
        # Return class-based view form_invalid to generate form with errors
        return self.form_invalid(form)

    def get_success_url(self, *args):
        return reverse('core:upload_image')


class ManageListImageListView(GaleryView, FormMixin):
    """List all photos to select the photos how must be on the Galery"""
    form_class = UploadImageManageForm
    template_name = 'manage_galery.html'

    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            super(ManageListImageListView, self).form_valid(form)
            messages.success(self.request, "Alterações realizadas com sucesso")
            return HttpResponseRedirect(self.get_success_url())
        self.object = None
        messages.error(self.request, f" {form.errors}")
        return self.form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ManageListImageListView, self).get_context_data(**kwargs)
        context['photos'] = GaleryPhoto.objects.all()
        return context

