# Generated by Django 3.0.7 on 2020-06-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_enable_null_proposalvote_scores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalvote',
            name='score',
            field=models.SmallIntegerField(blank=True, choices=[(3, '+1 — Good proposal and I will argue for it to be accepted.'), (1, '+0 — OK proposal, but I will not argue for it to be accepted.'), (0, 'n/a — I abstain from voting on this proposal.'), (-1, '−0 — Weak proposal, but I will not argue against acceptance.'), (-3, '−1 — Serious issues and I will argue to reject this proposal.')], null=True),
        ),
    ]