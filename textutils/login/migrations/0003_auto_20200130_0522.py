# Generated by Django 3.0.2 on 2020-01-29 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200130_0313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='emial',
            new_name='email',
        ),
    ]
