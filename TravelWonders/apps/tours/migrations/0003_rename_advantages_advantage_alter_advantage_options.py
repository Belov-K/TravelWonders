# Generated by Django 4.2.2 on 2023-07-11 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_advantages_hotel_detail_alter_tour_on_alter_tour_out'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advantages',
            new_name='Advantage',
        ),
        migrations.AlterModelOptions(
            name='advantage',
            options={'verbose_name': 'Преимущество', 'verbose_name_plural': 'Преимущества'},
        ),
    ]