from django.db import models
from django.contrib import messages


class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['course_name']) <= 5:
			errors['course_name'] = "Course name must be more than five characters"
		if len(postData['description']) <= 15:
			errors['description'] = 'Description must be more than 15 characters'
		return errors

class Course(models.Model):
	course_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	objects = CourseManager()

class Description(models.Model):
	description = models.CharField(max_length=255)
	course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)

	def __str__(self):
		return str(self.description)

class Comment(models.Model):
	comment = models.TextField()
	course = models.ForeignKey(Course, related_name="comments", on_delete = models.CASCADE)

	def __str__(self):
		return str(self.comment)