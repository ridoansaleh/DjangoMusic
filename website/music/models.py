from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    singer = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()

    def __unicode__(self):
        return self.title