from django.db import models

# Create your models here.
class News(models.Model):
    Title = models.CharField( max_length = 100, unique=True )
    Author = models.CharField(max_length = 70)
    Summary = models.CharField(max_length = 200,default='Short Text')
    Content = models.TextField()
    ImageName = models.TextField(default='name')
    Image = models.ImageField( )     
    Added_date = models.CharField(max_length=20) 
    Category = models.CharField(max_length=100)
    Sub_Category = models.CharField(max_length=100)
    Cat_ID = models.IntegerField(default="00")
    Sub_Cat_ID = models.IntegerField(default="00")
    Views = models.IntegerField(default="00")
    Count = models.IntegerField(default="00")
    #Category = models.ForeignKey(News_Cat, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

