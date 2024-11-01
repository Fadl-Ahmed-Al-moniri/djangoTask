from django.db import models as m 

# Create your models here.


class Category(m.Model):
    typename= m.CharField(max_length=255)

    def __str__(self) :
        return self.typename

class Book(m.Model):
    choices = [("available","available"),("sold","sold"),("rental","rental")]
    title= m.CharField(max_length=255,)
    author= m.CharField(max_length=255,null=True,blank=True)
    photobook = m.ImageField(upload_to='photos/%y/%m/%d',null=True,blank=True)
    photoauthor = m.ImageField(upload_to='photos/%y/%m/%d/author',null=True,blank=True)
    pages = m.IntegerField(null=True,blank=True)
    price=m.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    active= m.BooleanField(default=True)
    retal_price_day= m.DecimalField(max_digits=5,null=True,decimal_places=2,blank=True)
    retal_period= m.DecimalField(max_digits=5,null=True,decimal_places=2,blank=True)
    total_retal= m.DecimalField(max_digits=5,null=True,decimal_places=2,blank=True)
    state= m.CharField(max_length=50,null=True,choices=choices)
    typebook= m.ForeignKey(to= Category,  on_delete=m.PROTECT,null=True,blank=True)

    def __str__(self) : 
        return self.title
