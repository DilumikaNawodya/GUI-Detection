from django.conf import settings
from django.db import models
import os
from django.core.files.base import ContentFile
import json

# Create your models here.

def get_metajson_path(instance, filename):
    
    ext = filename.split('.')[-1]
    filename = "MetaJson-%s.%s" % (instance.id, ext)
    return os.path.join(settings.MEDIA_URL_METAJSON, filename)

def get_image_path(instance, filename):
    
    ext = filename.split('.')[-1]
    filename = "Image-%s.%s" % (instance.id, ext)
    return os.path.join(settings.MEDIA_URL_ORIGINAL, filename)


def get_finaljson_path(instance, filename):
    
    ext = filename.split('.')[-1]
    filename = "FinalJson-%s.%s" % (instance.id, ext)
    return os.path.join(settings.MEDIA_URL_FINALJSON, filename)

def get_detectedimage_path(instance, filename):
    
    ext = filename.split('.')[-1]
    filename = "DetectedImage-%s.%s" % (instance.id, ext)
    return os.path.join(settings.MEDIA_URL_DETECTED, filename)

class ImageJsonModel(models.Model):
    
    metajson = models.FileField(upload_to=get_metajson_path, null=True)
    image = models.FileField(upload_to=get_image_path, null=True)
    
    detectedimage = models.FileField(upload_to=get_detectedimage_path, null=True)
    finaljson = models.FileField(upload_to=get_finaljson_path, null=True)

    # Model Save override 
    def save(self, *args, **kwargs):
        if self.id is None:
            saved_image = self.image
            saved_metajson = self.metajson 
                    
            self.image = None
            self.metajson = None
            
            super(ImageJsonModel, self).save(*args, **kwargs)
            
            self.image = saved_image
            self.metajson = saved_metajson
            
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
                
        elif self.id is not None and self.detectedimage:
            
            saved_detectedimage = self.detectedimage
            self.detectedimage = None
            super(ImageJsonModel, self).save(*args, **kwargs)
            self.detectedimage = saved_detectedimage

            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
            
        super(ImageJsonModel, self).save(*args, **kwargs)
    
    def __str__(self):
        return "ImageJson " + str(self.id)