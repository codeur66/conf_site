# Generated by Django 2.2.10 on 2020-03-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0006_proposal_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='affiliation',
            field=models.CharField(max_length=200),
        ),
    ]