# Generated by Django 2.2.9 on 2020-03-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_auto_20200307_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='donors',
            name='mem_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]