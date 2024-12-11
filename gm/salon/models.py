from django.db import models

# Create your models here.

class Brend(models.Model):
    brend_name=models.CharField(max_length=150,unique=True,verbose_name='Kategoriya nomi')


    class Meta:
        verbose_name="Brend"
        verbose_name_plural='Brendlar'

    def __str__(self):
        return self.brend_name

class Cars(models.Model):
    brend=models.ForeignKey(Brend,on_delete=models.CASCADE,verbose_name='mashina brendi')
    model=models.CharField(max_length=100,verbose_name='mashina modeli')
    color=models.CharField(max_length=7,default='#FFFFFF',verbose_name='mashina rangi')
    photo=models.ImageField(upload_to='cars/',blank=True,null=True,verbose_name='mashina rasmi')
    probeg=models.IntegerField(default=0,verbose_name="mashina bosib o'tgan yo'li")
    max_speed=models.IntegerField(default=160,verbose_name='maximal tezligi')
    price=models.DecimalField(max_digits=12,decimal_places=2,verbose_name='mashina narxi')
    sotuvda_bormi=models.BooleanField(default=True,verbose_name='mashina sotuvda mavjud',
                                      help_text="Agar galochka qo'yilgan bo'lsa sotuvda bo bo'ladi")

    def __str__(self):
        return self.model


    class Meta:
        verbose_name="Mashina"
        verbose_name_plural='Mashinalar'
        ordering=['pk']


