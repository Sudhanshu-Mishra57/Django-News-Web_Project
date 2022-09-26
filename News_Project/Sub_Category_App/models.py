from django.db import models

# Create your models here.

class Sub_Category(models.Model):

    Title = models.CharField(max_length = 100, unique=True)
    Parent_Name = models.CharField(max_length=50)
    Parent_Id = models.IntegerField()
    Created_By = models.CharField(max_length= 25,default="Admin")
    Added_Date = models.CharField(max_length=20 ,default='dd-mm-yyyy') 
    Views = models.IntegerField(default="00")
    Short_Text = models.TextField()

    def __str__(self):
        return self.Title