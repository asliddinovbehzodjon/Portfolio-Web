# Generated by Django 4.0.2 on 2022-02-19 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_count_visitors_soni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xabar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=400)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Xabar',
                'verbose_name_plural': 'Xabarlar',
            },
        ),
    ]