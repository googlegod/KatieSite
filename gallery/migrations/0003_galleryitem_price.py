# Generated by Django 4.2.4 on 2023-09-04 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_galleryitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryitem',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
