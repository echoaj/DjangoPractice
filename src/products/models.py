from django.db import models

# Create your models here.
# Will map to DB
class Product(models.Model):
    title = models.CharField(max_length=25, blank=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    featured = models.BooleanField(null=True)

# null=True means all old values in the database just leave them empty when migrating new field
# or you can also do something like default=True