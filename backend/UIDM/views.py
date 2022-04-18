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
import cloudinary.uploader
from .KnowledgeBase.divert import divert

# Create your views here.


def pill(image_io):

    buffer = BytesIO()
    image_io.save(fp=buffer, format='JPEG')
    buff_val = buffer.getvalue()
    return ContentFile(buff_val)


def checkCompos(jsonFile):
    return len(jsonFile['combinedjson']['compos'])


@csrf_exempt
def CheckImage(request):

    if 'metajson' in request.FILES:

        instance = ImageJsonModel.objects.create(
            image=request.FILES['image'], metajson=request.FILES['metajson'])
        instance.save()

        # Check image
        results = CheckComponent(
            str(ImageJsonModel.objects.get(id=instance.id).image),
            str(ImageJsonModel.objects.get(id=instance.id).metajson)
        )

    else:

        instance = ImageJsonModel.objects.create(image=request.FILES['image'])
        instance.save()

        # Check image
        results = CheckComponent(
            str(ImageJsonModel.objects.get(id=instance.id).image)
        )

    img = Image.fromarray(results['combinedimage'], 'RGB')

    # Save detected image
    pillow_image = pill(img)
    image_file = InMemoryUploadedFile(
        pillow_image, None, 'foo.jpg', 'image/jpeg', pillow_image.tell, None)
    obj = ImageJsonModel.objects.filter(id=instance.id)[0]
    obj.detectedimage = image_file
    obj.save()

    # Json file
    obj = ImageJsonModel.objects.filter(id=instance.id)[0]
    obj.finaljson.save("json", ContentFile(
        str(json.dumps(results['combinedjson']))))

    # Upload to cloudinary
    upload_data = cloudinary.uploader.upload(obj.detectedimage)
    num_of_compos = checkCompos(results['combinedjson'])

    return JsonResponse({"combinedimage": upload_data, "no_of_compos": num_of_compos, "json_name": obj.finaljson.name}, status=200)


@csrf_exempt
def AddAnnotation(request):

    data = json.loads(request.body)

    accpeted_compo_list = []
    for compo in data['data']:
        accpeted_compo_list.append(compo['element'])

    key_val_compo = {}
    for compo in data['data']:
        key_val_compo[compo['element']] = compo['component']

    with open(os.path.join(settings.MEDIA_ROOT, data['name']), 'r+') as f:
        j_data = json.load(f)

        for compo in j_data['combinedjson']['compos']:
            if compo['id'] in accpeted_compo_list:
                compo['name'] = key_val_compo[compo['id']]
            else:
                compo['name'] = None

        for compo in j_data['combinedjson']['compos']:
            if 'embeddedcompos' in compo:
                for emb_compo in compo['embeddedcompos']:
                    if emb_compo['id'] in accpeted_compo_list:
                        emb_compo['name'] = key_val_compo[emb_compo['id']]
                    else:
                        emb_compo['name'] = None

        f.seek(0)
        json.dump(j_data, f)
        f.truncate()

        # KB comes here
        violated_ids = divert(j_data)

        return JsonResponse({"violated_ids": violated_ids}, status=200)
