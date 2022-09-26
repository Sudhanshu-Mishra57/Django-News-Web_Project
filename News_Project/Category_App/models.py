from django.db import models

# Create your models here.

class News_Category(models.Model):
    Title = models.CharField(max_length = 100, unique=True)
    Created_By = models.CharField(max_length= 40,default="Admin")
    Added_date = models.CharField(max_length=20) 
    Views = models.IntegerField(default="00")
    Short_Text = models.TextField()
    Count = models.IntegerField(default="0")

    def __str__(self):
        return self.Title   