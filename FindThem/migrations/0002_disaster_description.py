# Generated by Django 2.1.2 on 2018-10-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindThem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
