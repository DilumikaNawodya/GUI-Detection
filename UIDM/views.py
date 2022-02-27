from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import *
from .DetectionModel.runner import CheckComponent
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from tempfile import NamedTemporaryFile
from django.core.files import File


# Create your views here.

def pill(image_io):

    buffer = BytesIO()
    image_io.save(fp=buffer, format='JPEG')
    buff_val = buffer.getvalue()
    return ContentFile(buff_val)


@csrf_exempt
def CheckImage(request):

    instance = ImageJsonModel.objects.create(image = request.FILES['image'], metajson = request.FILES['metajson'])
    instance.save()
    
    # Check image
    results = CheckComponent(str(ImageJsonModel.objects.get(id=instance.id).image))
    img = Image.fromarray(results['combinedimage'], 'RGB')
    
    # Save detected image
    pillow_image  = pill(img)
    image_file = InMemoryUploadedFile(pillow_image, None, 'foo.jpg', 'image/jpeg', pillow_image.tell, None)
    obj = ImageJsonModel.objects.filter(id=instance.id)[0]
    obj.detectedimage = image_file
    obj.save()
    
    # Json file

    obj = ImageJsonModel.objects.filter(id=instance.id)[0]
    obj.finaljson.save("json", ContentFile(str(json.dumps(results['combinedjson']))))
    
    
    return JsonResponse({"combinedimage": obj.detectedimage.name, "combinedjson": results['combinedjson']}, status=200)
    

def AddAnnotation(request):
    
    return JsonResponse({"returnvalue": "Put return value here"}, status=200)
    

def Report(request):
    return JsonResponse({"returnvalue": "Put return value here"}, status=200)