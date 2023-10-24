# Generated by Django 4.2.6 on 2023-10-23 16:16

from django.db import migrations, models


def migrate_name(apps, schema_editor):
    UserProfile = apps.get_model("core", "UserProfile")
    db_alias = schema_editor.connection.alias
    for profile in UserProfile.all_objects.using(db_alias).all():
        profile.display_name = f"{profile.first_name} {profile.last_name}"
        profile.save()


def migrate_placeholders(apps, schema_editor):
    PlaceholderParticipation = apps.get_model("core", "PlaceholderParticipation")
    db_alias = schema_editor.connection.alias
    for placeholder in PlaceholderParticipation.objects.using(db_alias).all():
        placeholder.display_name = f"{placeholder.first_name} {placeholder.last_name}"
        placeholder.save()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0022_identityprovider"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="display_name",
            field=models.CharField(default="", max_length=254, verbose_name="name"),
            preserve_default=False,
        ),
        migrations.RunPython(migrate_name),
        migrations.RemoveField(
            model_name="userprofile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="last_name",
        ),
        migrations.AddField(
            model_name="placeholderparticipation",
            name="display_name",
            field=models.CharField(default="", max_length=254),
            preserve_default=False,
        ),
        migrations.RunPython(migrate_placeholders),
        migrations.RemoveField(
            model_name="placeholderparticipation",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="placeholderparticipation",
            name="last_name",
        ),
    ]