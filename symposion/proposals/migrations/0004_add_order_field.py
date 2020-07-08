# Generated by Django 3.0.8 on 2020-07-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_proposals', '0003_standardize_markdown_links'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proposalkind',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='proposalkind',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
            preserve_default=False,
        ),
    ]
