# Generated by Django 5.1.4 on 2025-01-06 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='contacts',
        ),
    ]
