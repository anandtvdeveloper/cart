from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='category')

    class Meta:
        ordering=('name',)
        verbose_name='category '
        verbose_name_plural='categories'

    def get_url(self):
            return reverse("cartdataapp:product_by_category", args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='product')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        verbose_name='product '
        verbose_name_plural='products'

    def get_url(self):
         return reverse("cartdataapp:acpdetail",args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
