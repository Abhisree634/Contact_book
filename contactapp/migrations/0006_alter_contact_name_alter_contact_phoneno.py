# Generated by Django 4.1.7 on 2023-09-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0005_contact_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phoneno',
            field=models.BigIntegerField(),
        ),
    ]
