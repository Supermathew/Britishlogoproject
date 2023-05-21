# Generated by Django 4.2.1 on 2023-05-21 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Navigation", "0003_rename_text2_footer_britishlogo_and_more"),
        ("Homepage", "0006_homepage_soccerblur"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="svg1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_svg1",
                to="Navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="svg2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_svg2",
                to="Navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="svg3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_svg3",
                to="Navigation.mediabucket",
            ),
        ),
    ]