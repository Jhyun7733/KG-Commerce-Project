# Generated by Django 4.0.3 on 2022-10-03 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='retitle',
            new_name='title',
        ),
    ]
