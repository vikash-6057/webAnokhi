# Generated by Django 2.2.4 on 2020-01-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0008_auto_20200131_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]