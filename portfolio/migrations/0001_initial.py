# Generated by Django 3.2.13 on 2022-06-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='portfolio/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
