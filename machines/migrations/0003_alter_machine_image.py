# Generated by Django 3.2.3 on 2021-06-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_alter_machine_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='image',
            field=models.FileField(upload_to='./uploads', verbose_name='image'),
        ),
    ]