from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(verbose_name='Enter category name', max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    title = models.CharField(verbose_name='Enter brand name', max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Product(models.Model):
    title = models.CharField(verbose_name='Product name', max_length=150, unique=True)
    description = models.TextField(verbose_name='Describe product')
    price = models.IntegerField(verbose_name='Price of product')
    quantity = models.IntegerField(verbose_name='Quantity of product')
    is_available = models.BooleanField(verbose_name='Is it availble now ?', default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class ProductImage(models.Model):
    photo = models.ImageField(verbose_name='Upload photo', upload_to='products/', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
