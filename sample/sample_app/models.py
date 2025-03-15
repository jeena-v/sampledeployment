from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='products/')    
    created=models.DateTimeField(auto_now_add=True,null=True)
