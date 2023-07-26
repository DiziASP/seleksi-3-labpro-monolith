from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    total = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.product
