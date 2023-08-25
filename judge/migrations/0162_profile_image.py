# Generated by Django 3.2.18 on 2023-08-24 00:50

from django.db import migrations, models
import judge.models.profile


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0161_auto_20230803_1536"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(
                null=True, upload_to=judge.models.profile.profile_image_path
            ),
        ),
    ]