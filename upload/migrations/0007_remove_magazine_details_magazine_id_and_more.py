# Generated by Django 4.0.4 on 2022-05-18 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_alter_magazine_upload_magazine_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine_details',
            name='magazine_id',
        ),
        migrations.RemoveField(
            model_name='magazine_upload',
            name='magazine_id',
        ),
        migrations.AddField(
            model_name='magazine_details',
            name='id',
            field=models.BigAutoField(auto_created=True, default=23, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
