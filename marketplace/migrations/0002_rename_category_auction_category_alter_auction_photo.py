# Generated by Django 4.1.4 on 2023-02-07 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='CATEGORY',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='auction',
            name='photo',
            field=models.ImageField(blank=True, upload_to='marketplace/'),
        ),
    ]
