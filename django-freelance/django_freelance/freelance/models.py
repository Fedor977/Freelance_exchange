from django.db import models
from django.contrib.auth.models import User


class Executor(models.Model):
    """Исполнитель"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f"User: {self.user}, phone: {self.user}"


class Customer(models.Model):
    """Заказчик"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f"User: {self.user}, phone: {self.user}"


class Service(models.Model):
    SERVICE_TYPE = [
        ('1', 'Разработка приложения'),
        ('2', 'Моделирование'),
        ('3', 'Разработка Data пайплайнов'),
        ('4', 'Разработка моделей машинного обучения')
    ]
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    service_type = models.CharField(choices=SERVICE_TYPE, default='1', max_length=1)

    def __str__(self):
        return f"{self.name} {self.get_service_type_display()} price: {self.price}"


class Order(models.Model):
    """Заказы"""
    SERVICE_TYPE = [
        ('1', 'Разработка приложения'),
        ('2', 'Моделирование'),
        ('3', 'Разработка Data пайплайнов'),
        ('4', 'Разработка моделей машинного обучения')
    ]
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    service_type = models.CharField(choices=SERVICE_TYPE, default='1', max_length=1)

    def __str__(self):
        return f"{self.name} {self.get_service_type_display()} price: {self.price}"


class Tag(models.Model):
    """Таг"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)


class Ordering(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField()
    deadline = models.DateTimeField()


class Messages(models.Model):
    """Сообщение"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    msg_date = models.BooleanField()
    is_edited = models.BooleanField(default=False)
    desc = models.TextField()


class Ticket(models.Model):
    SEVERITIES = [
        ('1', 'Низкая'),
        ('2', 'Средняя'),
        ('3', 'Высокая')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    severity = models.CharField(choices=SEVERITIES, default='1', max_length=1)
    desc = models.CharField(max_length=1000)
    ticket_date = models.DateField()
    is_resolved = models.BooleanField(default=False)


class Review(models.Model):
    RATING_FILLED = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    ]
    rating = models.CharField(choices=RATING_FILLED, default='1', max_length=1)
    desc = models.CharField(max_length=1000)


class Authoring(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    review_date = models.DateTimeField()

    def __str__(self):
        return f'{self.author} {self.review_date}'

