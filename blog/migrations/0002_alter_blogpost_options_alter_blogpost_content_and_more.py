# Generated by Django 5.1.1 on 2024-10-23 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogpost",
            options={
                "verbose_name": "Блоговая запись",
                "verbose_name_plural": "Блоговые записи",
            },
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="content",
            field=models.TextField(verbose_name="Содержимое"),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="preview_image",
            field=models.ImageField(
                upload_to="blog_previews/", verbose_name="Превью изображение"
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="published",
            field=models.BooleanField(default=False, verbose_name="Опубликовано"),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Заголовок"),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="views",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Количество просмотров"
            ),
        ),
    ]
