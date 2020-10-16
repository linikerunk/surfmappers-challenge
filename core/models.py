import datetime
from django.db import models
from stdimage import StdImageField, JPEGField
from django.core.files.storage import default_storage


class GaleryPhoto(models.Model):
    '''That class store all photos of the applications'''
    name = models.CharField("Nome", max_length=150, null=False)
    description = models.TextField("Descrição", blank=True) 
    image_date =  models.DateField("Date", default=datetime.date.today)
    image = StdImageField("Imagem", variations={
                         'thumbnail': {'width': 300, 'height': 300, "crop": True}})
    approved = models.BooleanField("Aprovado", default=False, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Galeria de Foto'
        verbose_name_plural = 'Galeria de Fotos'

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(GaleryPhoto, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name