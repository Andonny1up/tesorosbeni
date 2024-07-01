from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

# Create your models here.
class Category(models.Model):
    name = models.CharField('nombre',max_length=255)
    icon = models.ImageField('icono',upload_to='category_icons/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Pothole(models.Model):
    reported_by = models.CharField('reportado por',max_length=255, null=True, blank=True)
    phone = models.CharField('teléfono',max_length=15, null=True, blank=True)
    title = models.CharField('título',max_length=255, null=True, blank=True)
    description = models.TextField('descripción', null=True, blank=True)
    approved = models.BooleanField('aprobado',default=False)
    photo = models.ImageField('foto',upload_to='potholes/')
    thumbnail = ImageSpecField(source='photo',
                               processors=[ResizeToFit(300)],  # Cambia el tamaño de la imagen para que encaje en un cuadro de 800x800, manteniendo la relación de aspecto
                               format='JPEG',
                               options={'quality': 60})
    display_image = ImageSpecField(source='photo',
                                   processors=[ResizeToFit(800)],  # Para la imagen a mostrar en grande
                                   format='JPEG',
                                   options={'quality': 80})
    year_management = models.IntegerField('Gestión', null=True, blank=True)
    
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField('Ubicación', max_length=255, null=True, blank=True)
    province = models.CharField('Provincia',max_length=255, null=True, blank=True)
    municipality = models.CharField('Municipio',max_length=255, null=True, blank=True)
    discovery_date = models.DateField('Fecha del hallazgo',null=True, blank=True)


class PotholeImage(models.Model):
    pothole = models.ForeignKey(Pothole, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pothole_images/')
    thumbnail = ImageSpecField(source='photo',
                               processors=[ResizeToFit(300)],  # Cambia el tamaño de la imagen para que encaje en un cuadro de 800x800, manteniendo la relación de aspecto
                               format='JPEG',
                               options={'quality': 60})
    display_image = ImageSpecField(source='photo',
                                   processors=[ResizeToFit(800)],  # Para la imagen a mostrar en grande
                                   format='JPEG',
                                   options={'quality': 80})