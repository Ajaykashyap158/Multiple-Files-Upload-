# Generated by Django 4.0.4 on 2022-05-18 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_remove_magazine_details_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine_upload',
            name='magazine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meg_id', to='upload.magazine_details'),
        ),
    ]