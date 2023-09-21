# Generated by Django 4.2.4 on 2023-09-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0006_news_hotness"),
    ]

    operations = [
        migrations.DeleteModel(name="Image",),
        migrations.AddField(
            model_name="news",
            name="imgs_num",
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="news", name="pub_date", field=models.DateTimeField(),
        ),
    ]
