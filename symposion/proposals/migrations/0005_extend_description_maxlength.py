# Generated by Django 3.0.8 on 2020-07-31 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_proposals', '0004_add_order_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalbase',
            name='description',
            field=models.TextField(help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 400 characters.', max_length=2500, verbose_name='Brief Summary'),
        ),
    ]
