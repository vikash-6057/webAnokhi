# Generated by Django 2.2.9 on 2020-04-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_member_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='core',
            field=models.BooleanField(default=False),
        ),
    ]