# Generated by Django 4.2.2 on 2023-07-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название преимущества')),
                ('image', models.ImageField(upload_to='', verbose_name='фото')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('livingroom', models.ImageField(upload_to='', verbose_name='фото гостинной')),
                ('bedroom', models.ImageField(upload_to='', verbose_name='фото спальни')),
                ('hallway', models.ImageField(upload_to='', verbose_name='фото прихожей')),
            ],
            options={
                'verbose_name': 'Об отеле',
                'verbose_name_plural': 'Об отелях',
            },
        ),
        migrations.AlterField(
            model_name='tour',
            name='on',
            field=models.DateTimeField(verbose_name='туда'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='out',
            field=models.DateTimeField(verbose_name='обратно'),
        ),
    ]