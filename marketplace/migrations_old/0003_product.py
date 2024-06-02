# Generated by Django 5.0.3 on 2024-04-05 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_rename_category_photo_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('condition', models.CharField(choices=[('pre_owned', 'Pre-owned'), ('new_with_box', 'New with Box'), ('new_without_box', 'New without Box'), ('new_with_defects', 'New with Defects')], default='new_with_box', max_length=20)),
                ('description', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.department')),
            ],
        ),
    ]