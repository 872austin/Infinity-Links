from django.db import models

CATEGORY_CHOICES = [
    ('Necklace', 'Necklace'),
    ('Watch', 'Watch'),
    ('Bangle', 'Bangle'),
    ('Ring', 'Ring'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
