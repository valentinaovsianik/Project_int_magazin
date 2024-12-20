# Generated by Django 5.1.1 on 2024-10-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blogpost_options_alter_blogpost_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="preview_image",
            field=models.ImageField(upload_to="blog_previews/", verbose_name="Изображение"),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="published",
            field=models.BooleanField(default=False, verbose_name="Опубликовать"),
        ),
    ]
