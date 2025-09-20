from django.db import models
from django.core.validators import MinValueValidator


class People(models.Model):
    people_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    passport_series = models.CharField(max_length=10, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    passport_issued_by = models.TextField(blank=True, null=True)
    passport_issue_date = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'people'
        verbose_name = 'Арендатор'
        verbose_name_plural = 'Арендаторы'

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}"


class Apartment(models.Model):
    apartment_id = models.BigAutoField(primary_key=True)
    address = models.TextField()
    apartment_number = models.CharField(max_length=20, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    rooms_count = models.IntegerField(blank=True, null=True)
    total_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    living_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monthly_rent = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tenant = models.ForeignKey(
        People,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='apartments'
    )

    class Meta:
        db_table = 'apartment'
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

    def __str__(self):
        return f"Кв. {self.apartment_number}, {self.address}"


class Payment(models.Model):
    STATUS_CHOICES = [
        ('paid', 'Оплачено'),
        ('pending', 'В ожидании'),
        ('overdue', 'Просрочено'),
    ]

    payment_id = models.BigAutoField(primary_key=True)
    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    people = models.ForeignKey(
        People,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    period_month = models.IntegerField(
        validators=[MinValueValidator(1), MinValueValidator(12)]
    )
    period_year = models.IntegerField(
        validators=[MinValueValidator(2000), MinValueValidator(2100)]
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='paid')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payment'
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f"Платеж {self.payment_id} - {self.amount} руб."


class MaintenanceRequest(models.Model):
    STATUS_CHOICES = [
        ('open', 'Открыта'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]

    maintenance_request_id = models.BigAutoField(primary_key=True)
    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        related_name='maintenance_requests'
    )
    request_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    completion_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'maintenance_request'
        verbose_name = 'Заявка на обслуживание'
        verbose_name_plural = 'Заявки на обслуживание'

    def __str__(self):
        return f"Заявка #{self.maintenance_request_id} - {self.get_status_display()}"
