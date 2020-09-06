# Generated by Django 3.0.8 on 2020-08-12 09:52

from django.db import migrations, models
import software.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadableSoftware',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('downloadable_file', models.FileField(upload_to=software.models.case_upload_software_location)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=300)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamCarousel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('imgsrc', models.ImageField(blank=True, help_text='Upload The Image For The Team Carousel', upload_to='images/home/team')),
            ],
        ),
        migrations.CreateModel(
            name='TikTokLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('video_id', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('imgsrc', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopCarouseInHome',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, help_text='Upload The Image For The Home Carousel', upload_to='images/home/')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('imgsrc', models.URLField(blank=True)),
            ],
        ),
    ]