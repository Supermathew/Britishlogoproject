# Generated by Django 4.2.1 on 2023-05-21 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Navigation", "0003_rename_text2_footer_britishlogo_and_more"),
        ("Homepage", "0004_homepage_text27svg_homepage_text28svg_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="pencilimage",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_pencilimage",
                to="Navigation.mediabucket",
            ),
        ),
    ]