# Generated by Django 2.2.4 on 2020-03-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200321_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='memebers/'),
        ),
    ]