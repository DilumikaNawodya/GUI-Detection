# Generated by Django 3.2.3 on 2022-02-25 17:54

import UIDM.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UIDM', '0004_alter_imagejsonmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagejsonmodel',
            name='imagejson',
        ),
        migrations.RemoveField(
            model_name='imagejsonmodel',
            name='json',
        ),
        migrations.RemoveField(
            model_name='imagejsonmodel',
            name='textjson',
        ),
        migrations.AddField(
            model_name='imagejsonmodel',
            name='finaljson',
            field=models.FileField(null=True, upload_to=UIDM.models.get_finaljson_path),
        ),
        migrations.AddField(
            model_name='imagejsonmodel',
            name='metajson',
            field=models.FileField(null=True, upload_to=UIDM.models.get_metajson_path),
        ),
    ]