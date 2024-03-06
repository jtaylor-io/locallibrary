# Generated by Django 4.2.10 on 2024-03-06 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("abbreviation", models.CharField(max_length=2)),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name="book",
            name="language",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="catalog.language",
            ),
        ),
    ]