from django.db import models


class CustomerCL(models.Model):
    name = models.CharField("Имя:", max_length=50)
    surname = models.CharField("Фамилие:", max_length=50)
    address = models.CharField("Адрес доставки:", max_length=100)
    phone = models.CharField("Контакты:", max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField("TAG", max_length=50)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежда"

    name = models.CharField("Название:", max_length=50)
    image = models.ImageField("Фото:", upload_to='', null=True)
    price = models.PositiveIntegerField("Цена:")
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name


class OrderCL(models.Model):
    STATUS = (
        ("Ожидание", "Ожидание"),
        ("В пути", "В пути"),
        ("Доставка завершена", "Доставка завершена"),
    )
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(
        ProductCL, on_delete=models.CASCADE, related_name="order_product"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.product.name