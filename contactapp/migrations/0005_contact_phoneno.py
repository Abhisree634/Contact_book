# Generated by Django 4.1.7 on 2023-09-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0004_remove_contact_phoneno'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phoneno',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
