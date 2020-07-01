# Generated by Django 3.0.7 on 2020-07-01 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0005_change_first_time_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='affiliation',
            field=models.CharField(choices=[('C', 'Company'), ('S', 'School'), ('I', 'Independent')], max_length=1),
        ),
    ]
