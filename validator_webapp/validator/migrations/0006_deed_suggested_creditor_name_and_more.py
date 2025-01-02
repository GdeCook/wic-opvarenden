# Generated by Django 4.2.7 on 2023-11-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0005_deed_creditor_name_deed_creditor_uri_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deed',
            name='suggested_creditor_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='deed',
            name='suggested_debt_amount',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='deed',
            name='suggested_debt_amount_int',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]