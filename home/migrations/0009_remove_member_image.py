# Generated by Django 2.2.9 on 2020-03-29 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_member_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='image',
        ),
    ]
