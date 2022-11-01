from django.db import models

class Tweet(models.Model):
  name = models.CharField(max_length = 50)
  tweet = models.CharField(max_length = 50)
  datetime = models.DateTimeField(auto_now = True)
  
  def __str__(self):
    return self.name