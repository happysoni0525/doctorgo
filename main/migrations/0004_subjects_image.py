# Generated by Django 3.0.8 on 2020-08-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200807_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
