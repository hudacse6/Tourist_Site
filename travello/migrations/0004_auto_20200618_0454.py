# Generated by Django 3.0.6 on 2020-06-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_auto_20200617_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_blog',
            name='post_blog_summary',
            field=models.CharField(max_length=300),
        ),
    ]
