from django.db import models

# Create your models here.

PETROL_CHOICES = (
    (0, 'LPG'),
    (1, 'DIESEL'),
    (2, 'BENZINE'),
    (3, 'ELECTRIC')
)
class Company(models.Model):
    name = models.CharField(max_length=32)
    tax_number = models.IntegerField()

class Car(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    year = models.IntegerField()
    petrol = models.IntegerField(choices=PETROL_CHOICES)
    owner = models.ForeignKey(Company, on_delete=models.CASCADE, default="FIRMA XXX")
