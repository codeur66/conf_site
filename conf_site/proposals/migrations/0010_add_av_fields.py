# Generated by Django 3.0.7 on 2020-07-03 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0009_add_company_sponsor_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='av_equipment_needed',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes, audio'), (2, 'Yes, video'), (3, 'Yes, both')], default=0, verbose_name='Do you need audio and/or video recording equipment?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposal',
            name='av_needs',
            field=models.TextField(blank=True, verbose_name='If yes, describe your A/V needs.'),
        ),
    ]