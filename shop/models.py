from django.db import models


class Company(models.Model):
    logo = models.ImageField(upload_to='images/company/')
    title = models.CharField(max_length=123)
    description = models.TextField()
    phone = models.CharField(max_length=123)
    email = models.EmailField()
    address = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']


class Car(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    price = models.CharField(max_length=123)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name='cars', verbose_name='Особенности')
    benz = models.CharField(max_length=123, verbose_name='бензин')
    type = models.CharField(max_length=123, verbose_name='привод')
    сonsumption = models.CharField(max_length=123, verbose_name='КПП')
    power = models.CharField(max_length=123, verbose_name='Мощность')
    color = models.CharField(max_length=123, verbose_name='Цвет')
    rule = models.CharField(max_length=123, verbose_name='Руль')
    generation = models.CharField(max_length=123, verbose_name='Поколение')
    mileage = models.CharField(max_length=123, verbose_name='Пробег')
    year = models.CharField(max_length=123, verbose_name='Год')
    peculiarities = models.TextField(verbose_name='Особенности')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class CarImages(models.Model):
    product = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, related_name='images')
    images = models.ImageField(upload_to='images/%Y/%m/')

    def __str__(self):
        return f'{self.product.title} - {self.pk}'

    class Meta:
        verbose_name = 'Фотка машины'
        verbose_name_plural = 'Фотки машины'


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, related_name='orders')
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car.title} - {self.pk}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



