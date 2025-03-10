# Generated by Django 5.1.7 on 2025-03-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('job_url', models.URLField()),
                ('description', models.TextField()),
                ('is_remote', models.BooleanField(default=False)),
                ('job_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('grades', models.JSONField(default=dict)),
                ('interests', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
