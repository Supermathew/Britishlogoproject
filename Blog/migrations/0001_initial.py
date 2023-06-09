# Generated by Django 4.2.1 on 2023-05-21 08:27

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Navigation", "0003_rename_text2_footer_britishlogo_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blogauthor",
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
                ("bio", models.TextField()),
                ("Position", models.TextField()),
                ("name", models.CharField(max_length=225)),
                (
                    "profilephoto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Navigation.mediabucket",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("tag", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100, verbose_name="Post Title")),
                ("category", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "body",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name="Compose Content"
                    ),
                ),
                ("summary", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "Postauthor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Blog.blogauthor",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Blog.tag"
                    ),
                ),
                (
                    "thumbnail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Navigation.mediabucket",
                    ),
                ),
            ],
        ),
    ]
