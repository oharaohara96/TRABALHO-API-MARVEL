from django.db import migrations, models

# Generated by Django 4.0 on 2022-03-02 05:51


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_alter_category_title_alter_movie_sinopse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='censure',
            field=models.PositiveIntegerField(default=14),
            preserve_default=False,
        ),
    ]
