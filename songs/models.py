from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.db.models.functions import Lower

# Create your models here.

alphanumeric = RegexValidator(r'^[0-9a-zA-Z -]*$', 'Only alphanumeric characters are allowed.')
class Song(models.Model):
  name = models.CharField(max_length=30,validators=[alphanumeric])
  slug=models.SlugField(default="",blank=True,null=False,db_index=True)
  artist = models.CharField(max_length=30,validators=[alphanumeric])
  genre = models.CharField(max_length=30,validators=[alphanumeric])
  language = models.CharField(max_length=30,validators=[alphanumeric])
  image = models.ImageField(null=True,blank=True)
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super().save(*args,**kwargs)

  def __str__(self):
    return f"{self.name} by {self.artist}"
  
  # class Meta:
  #     constraints = [
  #         models.UniqueConstraint(
  #             Lower('<field name>'),
  #             name='<constraint name>'
  #         ),
  #     ]

class Yt(models.Model):
  pl_link = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  date = models.CharField(max_length=10)
  search = models.CharField(max_length=50)
