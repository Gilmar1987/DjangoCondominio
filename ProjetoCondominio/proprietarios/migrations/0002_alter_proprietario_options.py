# Generated by Django 5.2 on 2025-04-10 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proprietarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proprietario',
            options={'ordering': ['username'], 'verbose_name': 'Proprietário', 'verbose_name_plural': 'Proprietários'},
        ),
    ]
