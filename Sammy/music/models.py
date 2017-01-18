from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# Red pk=1 __ an xtra column is added with a unique identifier
class Album(models.Model):
  artist = models.CharField(max_length = 250)
  album_title = models.CharField(max_length = 250)
  genre = models.CharField(max_length = 100)
  album_logo = models.CharField(max_length = 1000)
  
  def get_absolute_url(self):    #whenever you create an album, redirect to the detail view with the pk
    return reverse('music:detail', kwargs={'pk':self.pk})
	
  def __str__(self):
    return self.album_title + ' - '+ self.artist

class Song(models.Model):
  album = models.ForeignKey( Album, on_delete = models.CASCADE)  
  #	Each song is associated with an Album. Whn you delete the album, 
  # delete(CASCADE)the Songs associted
  file_type = models.CharField(max_length = 10)
  song_title = models.CharField(max_length = 250)
  is_favorite = models.BooleanField(default = False)
  def __str__(self):
    return self.song_title