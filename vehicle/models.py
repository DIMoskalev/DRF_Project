from django.db import models

NULLABLE = {"blank": True, "null": True}


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='машина', **NULLABLE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, verbose_name='мотоцикл', **NULLABLE)

    milage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.SmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        return f'{self.milage} км пробега на {self.year} год'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробег'
        ordering = ('-year',)
