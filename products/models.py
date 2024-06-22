from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self' , verbose_name = _('parent') ,blank = True , null = True , on_delete = models.CASCADE)
    title = models.CharField(_("title") , max_lenght = 50 )
    description = models.TextField(_("description") , blank = True)
    avatar = models.ImageField(_("avatar") , blank = True , uplode_to = "categories/")
    is_enable = models.BooleanField(_("is_enable") , defualt = True)
    created_time = models.DateTimeField(_("created_time") , auto_now_add = True)
    updated_time = models.DateTimeField(_("updated_time") , auto_now = True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')



class Product(models.Model):
    title = models.CharField(_("title"), max_lenght=50)
    description = models.TextField(_("description"), blank=True)
    avatar = models.ImageField(_("avatar"), blank=True, uplode_to="products/")
    is_enable = models.BooleanField(_("is_enable"), defualt=True)
    categories = models.ManyToManyField('Category' , verbose_name =_('categories') , blank = True)
    created_time = models.DateTimeField(_("created_time"), auto_now_add=True)
    updated_time = models.DateTimeField(_("updated_time"), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')




class File(models.Model):
    products = models.ForeignKey('products', verbose_name = _('product') , on_delele = models.CASCADE)
    title = models.CharField(_("title"), max_lenght=50)
    file = models.FileField(_('file') , uplode_to = 'files/%y/%m/%d/')
    created_time = models.DateTimeField(_("created_time"), auto_now_add=True)
    updated_time = models.DateTimeField(_("updated_time"), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')



