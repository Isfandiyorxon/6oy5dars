from django.db import models

# Create your models here.

class Brend(models.Model):
    brend_name=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.brend_name

class Cars(models.Model):
    brend=models.ForeignKey(Brend,on_delete=models.CASCADE)
    model=models.CharField(max_length=100)
    color=models.CharField(max_length=7,default='#FFFFFF')
    photo=models.ImageField(upload_to='cars/',blank=True,null=True)
    probeg=models.IntegerField(default=0)
    max_speed=models.IntegerField(default=160)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    sotuvda_bormi=models.BooleanField(default=True)
    def __str__(self):
        return self.model




