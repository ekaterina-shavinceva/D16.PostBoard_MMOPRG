# Generated by Django 4.2.16 on 2024-11-01 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FanBoard_MMORPG', '0002_alter_article_author_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='upload',
        ),
    ]
