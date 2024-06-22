from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100) #имя поля
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/images/')
    description = models.TextField()
    created_at = models.DateTimeField
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
