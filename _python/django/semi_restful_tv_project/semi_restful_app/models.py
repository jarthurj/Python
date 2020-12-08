from django.db import models
import datetime
from datetime import date
from django.contrib import messages

class ShowManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		release_date = date.fromisoformat(postData['release_date'])
		if len(postData['title']) < 2:
			errors['title'] = "Show title should be at leaset 2 character"
		if len(postData['network']) < 3:
			errors['network'] = "Network should be longer thatn 3 characters"
		if len(postData['description']) < 10 and len(postData['description']) > 1:
			errors['description'] = "If a description is given it must be longer than 10 characters"
		if release_date > date.today():
			errors['release_date'] = "Release date should be in the past"	

		return errors

	def basic_and_edits(self, postData):
		errors = self.basic_validator(postData)
		for show in Show.objects.all():
			if show.title ==postData['title']:
				errors['title not unqiue'] = "Show already in database"
		return errors
class Show(models.Model):
	title = models.CharField(max_length=255)
	network = models.CharField(max_length=255)
	release_date = models.DateField(auto_now=False, auto_now_add=False)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ShowManager()
	def __repr__(self):
		return f"{self.title}, {self.network}, {self.release_date}"

