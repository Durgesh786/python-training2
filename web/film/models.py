from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Language(models.Model):

    name = models.TextField(null=False)
    last_update = models.DateTimeField(_("Last Updated Date"), auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        db_table = "language"
        verbose_name_plural = "Film Language"

class Category(models.Model):

    name=models.TextField(null=False)
    last_update=models.DateTimeField(_("Last Updated Date"),auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name_plural = "Film Category"



class Films(models.Model):

    language = models.ForeignKey(to=Language,on_delete=models.CASCADE, related_name='film_language')
    rental_duration=models.IntegerField(null=False)
    rental_rate=models.DecimalField(null=False,max_digits=2,decimal_places=2)
    length=models.TextField(null=False)
    replacement_cost=models.DecimalField(null=False,max_digits=2,decimal_places=2)
    rating=models.TextField(null=False)
    special_features=models.TextField(null=False)
    fulltext=models.TextField(null=False)
    title=models.TextField(null=False)
    release_year=models.IntegerField(null=False)
    description = models.TextField(null=False)
    last_update = models.DateTimeField(_("Last Updated Date") ,auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        db_table = "film"
        verbose_name_plural = "Film"

class FilmCategory(models.Model):
    film=models.ForeignKey(to=Films, null=False, on_delete=models.CASCADE, related_name="film_category_film")
    category=models.ForeignKey(to=Category,on_delete=models.CASCADE,null=False,related_name="film_category_category")
    last_update=models.DateTimeField(_("Last Updated Date"),auto_now=True)

    def __str__(self):
        return "{}".format(self.film)

    class Meta:
        db_table = "film_category"
        verbose_name_plural = "Films Category"

class Actor(models.Model):
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    last_update = models.DateTimeField(_("Last Updated Date"), auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

    class Meta:
        db_table = "actor"
        verbose_name_plural = "Actors Profile"


class FilmActor(models.Model):
    film=models.ForeignKey(to=Films, null=False, on_delete=models.CASCADE, related_name="film_actor_film")
    actor=models.ForeignKey(to=Actor,null=False,on_delete=models.CASCADE,related_name="film_actor_actor")
    last_update=models.DateTimeField(_("Last Updated Date"),auto_now=True)

    def __str__(self):
        return "{}".format(self.actor)

    class Meta:
        db_table = "film_actor"
        verbose_name_plural = "Film Actor"
