from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
from web.film.models import Films


class Country(models.Model):

    country = models.TextField(null=True)
    updated_ts = models.DateTimeField(_("Last Updated Date"), auto_now=True)

    def __str__(self):
        return self.country

    class Meta:
        db_table = "country"
        verbose_name_plural = "country"

class City(models.Model):
    country=models.ForeignKey(to=Country,on_delete=models.CASCADE,related_name="country_city")
    city=models.TextField(null=True)
    last_update=models.DateTimeField(_("Last Updated Date"),auto_now=True)

    def __str__(self):
        return self.city

    class Meta:
        db_table = "city"
        verbose_name_plural = "City name"



class Address(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_profile', null=True)
    city = models.ForeignKey(to=City,on_delete=models.CASCADE, related_name='city_address')
    address=models.TextField(null=False)
    address2=models.TextField(null=True)
    district=models.TextField(null=False)
    postal_code=models.IntegerField(null=False)
    phone=models.IntegerField(null=False)
    last_update = models.DateTimeField(_("Last Updated Date"), auto_now=True)

    def __str__(self):
        return "{}".format(self.address)


    class Meta:
        db_table = "address"
        verbose_name_plural = "All Address"

class Store(models.Model):
    manager_staff=models.ForeignKey(to=User,null=False,on_delete=models.CASCADE,related_name="store_staff")
    address=models.ForeignKey(to=Address,null=False,on_delete=models.CASCADE,related_name="store_address")
    last_update=models.DateTimeField(_("Last Updated Date"),auto_now=True)

    def __str__(self):
        return "{}".format(self.address)

    class Meta:
        db_table = "store"
        verbose_name_plural = "Store"

class Inventory(models.Model):
    film = models.ForeignKey(to=Films, on_delete=models.CASCADE, related_name="inventory_film", null=False)
    store = models.ForeignKey(to=Store,on_delete=models.CASCADE,related_name="inventory_store",null=False)
    last_update = models.DateTimeField(_("Last Updated Date"), auto_now=True)

    def __str__(self):
        return "{}".format(self.film)

    class Meta:
        db_table = "inventory"
        verbose_name_plural = "film stock"


class Rental(models.Model):
    return_date=models.DateField(null=False)
    inventory=models.ForeignKey(to=Inventory,null=False,on_delete=models.CASCADE,related_name="rental_inventory")
    customer=models.ForeignKey(to=User,null=False,on_delete=models.CASCADE,related_name="rental_customer")
    rental_date=models.DateField(null=False)
    staff=models.ForeignKey(to=User,null=False,on_delete=models.CASCADE,related_name="rental_staff")
    last_update=models.DateTimeField(_("Last Update Date"),auto_now=True)

    def __str__(self):
        return "{}".format(self.customer)

    class Meta:
        db_table = "rental"
        verbose_name_plural = "Rental"

class Payment(models.Model):
    payment_date=models.DateField(null=False)
    amount=models.DecimalField(null=False,max_digits=2,decimal_places=2)
    rental=models.ForeignKey(to=Rental,null=False,on_delete=models.CASCADE,related_name="payment_rental")
    staff=models.ForeignKey(to=User,null=False,on_delete=models.CASCADE,related_name="payment_staff")
    customer=models.ForeignKey(to=User,null=False,on_delete=models.CASCADE,related_name="payment_customer")

    def __str__(self):
        return "{}".format(self.customer)

    class Meta:
        db_table = "payment"
        verbose_name_plural = "Payment"