from django.db import models
from django.template.backends import django
from django.utils import timezone as tz


class ItemToBuy(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default=None, verbose_name="Наименование")
    description = models.TextField(default=None, verbose_name="Описание")
    sizes = models.CharField(max_length=200, default="-", verbose_name="Размеры")
    number = models.IntegerField(default=1, verbose_name="Количество")
    estimate_price = models.DecimalField(decimal_places=2, max_digits=int(20), null=True, verbose_name="Ожидаемая цена")
    created_date = models.DateField(
            default=tz.now, verbose_name="Дата добавления")
    estimate_date = models.DateField(
            blank=True, null=True, verbose_name="Сроки до")

    def publish(self):
        self.published_date = tz.now()
        self.save()

    def __str__(self):
        return self.title

