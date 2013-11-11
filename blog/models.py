from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 50)
    headImg = models.FileField(upload_to = './upload/')

    def __unicode__(self):
	return self.name
