# Generated by Django 3.0.8 on 2020-07-18 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('callnum', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=50)),
                ('established_on', models.DateField()),
                ('employees_cnt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects_name', models.CharField(max_length=20)),
                ('specialist_cnt', models.IntegerField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=10)),
                ('contents', models.TextField()),
                ('speed', models.IntegerField()),
                ('kindness', models.IntegerField()),
                ('responsibility', models.IntegerField()),
                ('professionality', models.IntegerField()),
                ('disliked_users', models.ManyToManyField(related_name='disliked_reviews', to=settings.AUTH_USER_MODEL)),
                ('liked_users', models.ManyToManyField(related_name='liked_reviews', to=settings.AUTH_USER_MODEL)),
                ('subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Subjects')),
            ],
        ),
    ]
