from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self' , verbose_name = ('parent') ,blank = True , null = True , on_delete =models.CASCADE)
    title = models.CharField(("title") , max_length = 50 )
    description = models.TextField(("description") , blank = True)
    avatar = models.ImageField(("avatar") , blank = True , upload_to= 'categories/')
    is_enable = models.BooleanField(("is_enable") , default = True)
    created_time = models.DateTimeField(("created_time") , auto_now_add = True)
    updated_time = models.DateTimeField(("updated_time") , auto_now = True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Products(models.Model):
    title = models.CharField(("title"), max_length=50)
    description = models.TextField(("description"), blank=True)
    avatar = models.ImageField(("avatar"), blank=True, upload_to='products/')
    is_enable = models.BooleanField(("is_enable"), default=True)
    categories = models.ManyToManyField('Category' , verbose_name =('categories') , blank = True)
    created_time = models.DateTimeField(("created_time"), auto_now_add=True)
    updated_time = models.DateTimeField(("updated_time"), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'






class File(models.Model):
    products = models.ForeignKey('products', verbose_name = ('product') , on_delete = models.CASCADE)
    title = models.CharField(("title"), max_length=50)
    file = models.FileField(('file') , upload_to = 'files/%y/%m/%d/')
    created_time = models.DateTimeField(("created_time"), auto_now_add=True)
    updated_time = models.DateTimeField(("updated_time"), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = ('file')
        verbose_name_plural = ('files')



