from django.db import models

# Create your models here.

class Contact(models.Model):
    Name       = models.CharField( max_length = 100)
    Email      = models.EmailField()
    Subject    = models.CharField( max_length=200 )
    Message    = models.TextField()
    Added_date = models.CharField(max_length=20 ,default='dd-mm-yyyy') 
    def __str__(self):
        return self.Title