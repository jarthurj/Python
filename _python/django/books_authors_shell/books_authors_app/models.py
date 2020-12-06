from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	#authors = list of authors that worked on this book

	def __repr__(self):
		ret_str = self.title + " " + self.desc + " " +str(self.authors)
		return ret_str
class Author(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	notes = models.TextField()
	books = models.ManyToManyField(Book, related_name="authors")


	def __repr__(self):
		ret_str = self.first_name + " " + self.last_name + " " + str(self.books)
		return ret_str