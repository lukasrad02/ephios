# Generated by Django 3.2.7 on 2021-09-03 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_auto_20210903_1258"),
    ]

    operations = [
        migrations.RenameField(
            model_name="qualification",
            old_name="included_qualifications",
            new_name="includes",
        ),
    ]