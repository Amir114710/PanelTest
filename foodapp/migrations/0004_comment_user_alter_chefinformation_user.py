# Generated by Django 4.2.3 on 2023-11-25 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("foodapp", "0003_rename_foodinformation_chefinformation"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment",
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="chefinformation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chefs",
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
        ),
    ]
