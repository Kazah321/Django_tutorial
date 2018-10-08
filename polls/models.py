import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

class Calculator(models.Model):
	suma = models.IntegerField(default=0)
	def calc_add(self,a,b):
		 suma = a+b
		 return suma
	def calc_sub(self,a,b):
		return a-b
	def calc_sq(self,a):
		return a*a
	def calc_div(self,a,b):
		return a/b
	def calc_mul(self,a,b):
		return a*b
