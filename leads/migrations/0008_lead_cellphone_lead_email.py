# Generated by Django 4.1.4 on 2023-02-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_lead_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='cellphone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
