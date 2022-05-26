# Generated by Django 4.0.4 on 2022-05-26 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=64)),
                ('image_file', models.ImageField(upload_to=pathlib.PurePosixPath('uploads'))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
