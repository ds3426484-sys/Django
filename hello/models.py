from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=200, verbose_name="Имя")
    surname = models.CharField(max_length=200, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=200, blank=True, default="", verbose_name="Отчество")

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="Название категории")
    comment = models.TextField(max_length=500, verbose_name="Комментарий")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="Название товара")
    sale = models.IntegerField(default=0, verbose_name="Цена")
    material = models.CharField(max_length=100, default="", verbose_name="Материал")
    date_prod = models.DateField(default=timezone.now, verbose_name="Дата производства")
    counter = models.IntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True,
        verbose_name="Категория",
        db_column='cat_id_id'  # ← ДОБАВЛЕНО: указываем реальное имя поля в БД
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"