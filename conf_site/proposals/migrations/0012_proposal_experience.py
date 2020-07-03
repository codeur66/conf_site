# Generated by Django 3.0.8 on 2020-07-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0011_add_stipend_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='experience',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Have you presented at a conference before?'),
        ),
    ]
