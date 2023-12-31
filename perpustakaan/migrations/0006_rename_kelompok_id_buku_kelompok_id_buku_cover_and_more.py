# Generated by Django 5.0 on 2023-12-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0005_buku_kelompok_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buku',
            old_name='Kelompok_id',
            new_name='kelompok_id',
        ),
        migrations.AddField(
            model_name='buku',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
        migrations.AddField(
            model_name='buku',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
