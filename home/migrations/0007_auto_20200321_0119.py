# Generated by Django 2.2.9 on 2020-03-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200320_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='batch',
            field=models.CharField(blank=True, default='-1', max_length=100, null=True),
        ),
    ]
