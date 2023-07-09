from django.db import models

class Tour(models.Model):
    image=models.ImageField('картинка')
    name=models.CharField('название отеля', max_length=50)
    country=models.CharField('страна', max_length=50)
    city=models.CharField('город', max_length=50)
    price=models.CharField('цена', max_length=50)
    star=models.FloatField('звезды')
    tour=models.FloatField('сколько туров')

    class Meta:
        verbose_name="Тур"
        verbose_name_plural="Туры"

    def __str__(self):
        return self.name