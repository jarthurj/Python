from django.db import models

class Dojo(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	desc = models.TextField(default="Old Dojo")
	#ninjas = list of ninjas at this dojo

	def __repr__(self):
		ret_str = self.name + self.city + self.state
		return ret_str

class Ninja(models.Model):
	dojo = models.ForeignKey(Dojo, related_name = "ninjas", on_delete = models.CASCADE)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	def __repr__(self):
		ret_str = self.dojo + self.first_name + self.last_name
		return ret_str