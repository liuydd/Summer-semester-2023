# Generated by Django 4.2.4 on 2023-09-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0008_news_comment_num"),
    ]

    operations = [
        migrations.RemoveField(model_name="news", name="comment_num",),
        migrations.AddField(
            model_name="news",
            name="comment_count",
            field=models.IntegerField(default=0),
        ),
    ]
