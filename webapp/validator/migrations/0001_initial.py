# Generated by Django 4.0.3 on 2023-06-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deed_uri', models.URLField(unique=True)),
                ('deed_date', models.DateField()),
                ('final_name', models.CharField(blank=True, max_length=200, verbose_name='Name')),
                ('final_location', models.CharField(blank=True, max_length=200, verbose_name='Location')),
                ('final_ship_name', models.CharField(blank=True, max_length=200, verbose_name='Ship')),
                ('final_role', models.CharField(blank=True, max_length=200, verbose_name='Role')),
                ('final_organization', models.CharField(blank=True, max_length=200, verbose_name='Organization')),
                ('suggested_name', models.CharField(blank=True, max_length=200)),
                ('suggested_location', models.CharField(blank=True, max_length=200)),
                ('suggested_role', models.CharField(blank=True, max_length=200)),
                ('suggested_organization', models.CharField(blank=True, max_length=200)),
                ('suggested_ship_name', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('organization', models.CharField(blank=True, max_length=255, null=True)),
                ('ship_name', models.CharField(blank=True, max_length=255, null=True)),
                ('location_htr', models.CharField(blank=True, max_length=255, null=True)),
                ('role_htr', models.CharField(blank=True, max_length=255, null=True)),
                ('organization_htr', models.CharField(blank=True, max_length=255, null=True)),
                ('ship_name_htr', models.CharField(blank=True, max_length=255, null=True)),
                ('sailor_uri', models.URLField(blank=True, null=True)),
                ('location_uri', models.URLField(blank=True, null=True)),
                ('interesting_text', models.TextField(blank=True, null=True)),
                ('interesting_text_after', models.TextField(blank=True, null=True)),
                ('possible_names', models.TextField(blank=True, null=True)),
                ('possible_locations', models.TextField(blank=True, null=True)),
                ('subject', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('full_coords', models.TextField(blank=True, null=True)),
                ('dimensions', models.TextField(blank=True, null=True)),
                ('image_url', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
