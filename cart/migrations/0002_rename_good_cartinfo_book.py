# Generated by Django 5.0.6 on 2024-06-02 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartinfo',
            old_name='good',
            new_name='book',
        ),
    ]
