from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
	# the Topic class stores the data of a single topic type in our site
	text = models.CharField(max_length=200) # this is for setting the topic name
	date_added = models.DateTimeField(auto_now_add=True) # getting the creation time
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		# this method will be used by framework to show the output of the object
		return self.text

class Entry(models.Model):
	# each Entry class contains a name and a Topic
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)	
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Mets:
		versose_name_plural = 'entries'

	def __str__(self):
		return f'{self.text[:50]}...'		
