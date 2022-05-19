# Generated by Django 4.0.4 on 2022-05-18 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_alter_magazine_upload_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine_details',
            name='id',
        ),
        migrations.AddField(
            model_name='magazine_details',
            name='magazine_id',
            field=models.IntegerField(default=23, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magazine_upload',
            name='magazine_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='meg_id', to='upload.magazine_details'),
        ),
        migrations.AlterField(
            model_name='magazine_upload',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
