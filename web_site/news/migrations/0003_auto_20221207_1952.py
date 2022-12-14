# Generated by Django 3.2.16 on 2022-12-07 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articles_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Статьи', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='anons',
            field=models.CharField(max_length=250, verbose_name='Год издания'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_text',
            field=models.TextField(verbose_name='ФИО Автора'),
        ),
    ]
