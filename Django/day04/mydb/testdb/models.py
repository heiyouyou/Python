# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)

class Persons(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Fruit(models.Model):
	name = models.CharField(max_length=100,primary_key=True)
	price = models.DecimalField(max_digits=20,decimal_places=2)

# 多对一的关系
class Reporter(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()

	def __unicode__(self):
		return "%s %s" %(self.first_name,self.last_name)

class Article(models.Model):
	headline = models.CharField(max_length=30)
	pub_date = models.DateField()
	reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)

	def __unicode__(self):
		return self.headline

	class Meta:
		ordering = ('headline',)

# 多对多的关系
class Publication(models.Model):
	title = models.CharField(max_length=100)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('title',)

class Articles(models.Model):
	headline = models.CharField(max_length=100)
	publications = models.ManyToManyField(Publication)

	def __unicode__(self):
		return self.headline

	class Meta:
		ordering = ('headline',)

# 自定义多对多的关系
class Group(models.Model):
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(Person,through='Membership')

	def __unicode__(self):
		return self.name

class Membership(models.Model):
	person = models.ForeignKey(Person,on_delete=models.CASCADE)
	group = models.ForeignKey(Group,on_delete=models.CASCADE)
	date_joined = models.DateField()
	invite_reason = models.CharField(max_length=64)

# 一对一的关系
class Place(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=80)
	def __unicode__(self):
		return "%s the place" % self.name

class Restaurant(models.Model):
	place = models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)
	serves_hot_dogs = models.BooleanField(default=False)
	serves_pizza_dogs = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s the restaurant" % self.place.name

class Waiter(models.Model):
	restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return "%s the waiter at %s" % (self.name,self.restaurant)