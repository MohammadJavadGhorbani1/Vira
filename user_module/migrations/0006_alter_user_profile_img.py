# Generated by Django 5.0.7 on 2024-07-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0005_alter_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='profile_images', verbose_name='تصویر پروفایل'),
        ),
    ]