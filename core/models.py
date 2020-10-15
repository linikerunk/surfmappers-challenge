import datetime
from django.db import models
from stdimage import StdImageField, JPEGField
from django.core.files.storage import default_storage


PHOTOS_FOLDER = "media/"
DEFAULT = '0000.jpg'

class GaleryPhoto(models.Model):
    '''That class store all photos of the applications'''
    name = models.CharField("Nome", max_length=150, null=False)
    description = models.TextField("Descrição", blank=True) 
    image_date =  models.DateField("Date", default=datetime.date.today)
    image = StdImageField("Imagem", upload_to='media/', variations={
                         'thumbnail': {'width': 300, 'height': 175}})
    approved = models.BooleanField("Aprovado", default=False, null=True)
    
    class Meta:
        verbose_name = 'Galeria de Foto'
        verbose_name_plural = 'Galeria de Fotos'

    def get_image_url(self):
        path = f'{PHOTOS_FOLDER}/{self.image}.jpg'

        if default_storage.exists(path):
            return default_storage.open(path).name

        return default_storage.open(f'{PHOTOS_FOLDER}/{DEFAULT}').name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(GaleryPhoto, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


    




