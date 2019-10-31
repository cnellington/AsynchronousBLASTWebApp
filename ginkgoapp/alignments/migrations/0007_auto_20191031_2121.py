# Generated by Django 2.2.6 on 2019-10-31 21:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alignments', '0006_auto_20191031_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protein',
            name='reference',
        ),
        migrations.AddField(
            model_name='protein',
            name='file',
            field=models.FileField(default='', upload_to='protein_files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['fasta'])]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='protein',
            name='name',
            field=models.CharField(default='unprocessed', max_length=16),
        ),
        migrations.AddField(
            model_name='protein',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Processed', 'Processed')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='alignment',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Processed', 'Processed')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='protein',
            name='description',
            field=models.CharField(default='unprocessed', max_length=128),
        ),
    ]
