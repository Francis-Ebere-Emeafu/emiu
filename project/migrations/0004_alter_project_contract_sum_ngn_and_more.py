# Generated by Django 4.0.2 on 2022-08-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_description_alter_project_lga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contract_sum_ngn',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='contract_sum_usd',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=50, null=True),
        ),
    ]
