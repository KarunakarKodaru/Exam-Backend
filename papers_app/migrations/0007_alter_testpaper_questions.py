# Generated by Django 4.0.5 on 2022-07-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers_app', '0006_rename_cut_0ff_marks_testpaper_cut_off_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testpaper',
            name='questions',
            field=models.ManyToManyField(default=[], to='papers_app.question'),
        ),
    ]
