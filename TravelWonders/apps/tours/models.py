from django.db import models

class Hotel(models.Model):
    image=models.ImageField('картинка')
    name=models.CharField('название отеля', max_length=50)
    country=models.CharField('страна', max_length=50)
    city=models.CharField('город', max_length=50)
    price=models.CharField('цена', max_length=50)
    star=models.FloatField('звезды')
    tourr=models.FloatField('сколько туров')

    class Meta:
        verbose_name="Отель"
        verbose_name_plural="Отели"

    def __str__(self):
        return self.name

class Tour(models.Model):

    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)

    on=models.DateTimeField('туда')
    out=models.DateTimeField('обратно')
    name=models.CharField('название тура', max_length=50)
    price=models.IntegerField('цена')

    class Meta:
        verbose_name="Тур"
        verbose_name_plural="Туры"

class City(models.Model):
    image=models.ImageField('картинка')
    name_city=models.CharField('название города', max_length=50)
    price=models.IntegerField('цена')
    country=models.CharField('город', max_length=50)

    class Meta:
        verbose_name="Город"
        verbose_name_plural="Города"

    def __str__(self):
        return self.name_city

class Hotel_detail(models.Model):
    name=models.CharField('название', max_length=50)
    livingroom=models.ImageField('фото гостинной')
    bedroom=models.ImageField('фото спальни')
    hallway=models.ImageField('фото прихожей')

    class Meta:
        verbose_name="Об отеле"
        verbose_name_plural="Об отелях"

    def __str__(self):
        return self.name

class Advantages(models.Model):
    name=models.CharField('название преимущества', max_length=50)
    image=models.ImageField('фото')

    def __str__(self):
        return self.name