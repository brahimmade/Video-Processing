# Generated by Django 3.0.4 on 2020-03-16 14:53

import core.models
import core.storage
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoSubmission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_name', models.TextField()),
                ('status', models.CharField(default='in_queue', max_length=10)),
                ('video', models.FileField(upload_to=core.models.get_video_path, validators=[core.models.validate_video])),
                ('subtitle', models.FileField(upload_to=core.models.get_subtitle_path, validators=[core.models.validate_subtitle])),
                ('total_chunks', models.SmallIntegerField(default=0)),
                ('processed_video', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='VideoChunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chunk_no', models.SmallIntegerField()),
                ('video_chunk', models.FileField(upload_to='')),
                ('audio_chunk', models.FileField(storage=core.storage.OverwriteStorage(), upload_to=core.models.get_audio_chunk_path, validators=[core.models.validate_audio])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('subtitle', models.TextField()),
                ('VideoSubmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.VideoSubmission')),
            ],
        ),
    ]
