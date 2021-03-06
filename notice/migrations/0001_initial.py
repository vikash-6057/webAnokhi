# Generated by Django 2.2.9 on 2022-02-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='notices/')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'notices',
            },
        ),
    ]
