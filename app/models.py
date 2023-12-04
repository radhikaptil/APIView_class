from django.db import models

# Create your models here.

class Product_catagory(models.Model):
    catagory_name=models.CharField(max_length=100)
    catagory_id=models.IntegerField()

    def __str__(self):
        return self.catagory_name
    

class Product(models.Model):
    catagory_name=models.ForeignKey(Product_catagory,on_delete=models.CASCADE)
    Product_name=models.CharField(max_length=100)
    Pid=models.IntegerField()
    Price=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self) -> str:
        return self.Product_name
    
    
    
    

