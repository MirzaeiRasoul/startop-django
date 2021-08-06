# Generated by Django 3.2.6 on 2021-08-05 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Startop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('subtitle', models.CharField(blank=True, default='', max_length=500)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]