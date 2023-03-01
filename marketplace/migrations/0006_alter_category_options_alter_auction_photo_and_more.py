# Generated by Django 4.1.4 on 2023-03-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_category_alter_auction_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-pk',)},
        ),
        migrations.AlterField(
            model_name='auction',
            name='photo',
            field=models.ImageField(blank=True, default='blank/blank.jpg', upload_to='marketplace/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Other', max_length=50, unique=True),
        ),
    ]
