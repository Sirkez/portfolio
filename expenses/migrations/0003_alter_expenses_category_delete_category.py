# Generated by Django 4.1.4 on 2023-03-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_expenses_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]