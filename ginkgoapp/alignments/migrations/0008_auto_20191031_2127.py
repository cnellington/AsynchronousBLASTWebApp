# Generated by Django 2.2.6 on 2019-10-31 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alignments', '0007_auto_20191031_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protein',
            name='description',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='protein',
            name='name',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
