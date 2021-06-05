# Generated by Django 3.2.3 on 2021-06-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('image', models.FileField(upload_to='', verbose_name='image')),
            ],
        ),
    ]