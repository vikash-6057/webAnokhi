# Generated by Django 2.2.9 on 2020-03-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='mob',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='name',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='mem_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
