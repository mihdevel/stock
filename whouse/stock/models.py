from django.db import models
from django.utils import timezone

class Product(models.Model):
	"""docstring for Product"""
	name = models.CharField(max_length=30)
	quantity = models.IntegerField(default=0)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	sale = models.ForeignKey('Sale', on_delete=models.CASCADE)
	price = models.FloatField()
	date_add = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Group(models.Model):
	"""docstring for Group"""
	name = models.CharField(max_length=30)
	date_add = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name


class Sale(models.Model):
	"""docstring for Sale"""
	name = models.CharField(max_length=30)
	percent = models.IntegerField()
	date_add = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name