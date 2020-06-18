# Generated by Django 2.2.13 on 2020-06-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100)),
                ('audience', models.IntegerField(default=0)),
                ('open_date', models.DateField()),
                ('genre', models.CharField(max_length=100)),
                ('watch_grade', models.CharField(max_length=100)),
                ('score', models.FloatField(default=0)),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
