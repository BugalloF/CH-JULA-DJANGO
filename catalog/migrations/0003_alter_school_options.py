# Generated by Django 4.1 on 2022-08-26 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_person_friends'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['quantity']},
        ),
    ]
