# Generated by Django 3.1.6 on 2021-02-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='uploadTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
