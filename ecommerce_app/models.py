from django.db import models


class category_model(models.Model):
    cat_name= models.CharField(max_length=200)
    cat_store= models.CharField(max_length=200)

class product_model(models.Model):
    cat_table=models.ForeignKey(category_model,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=200)
    product_quantity=models.IntegerField()
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to='image/')







# Create your models here.
