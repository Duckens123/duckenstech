from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Article(models.Model):
    #category= models.ForeignKey(Category,related_name="category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    content = models.TextField(blank=True, null=True)
    datepublished= models.DateTimeField(auto_now_add=True)
    lastupdated= models.DateTimeField(auto_now=True)
    publishedby= models.ForeignKey(User,  on_delete=models.CASCADE)
    imagethumbnail= CloudinaryField('image')
    imagecaptions= models.CharField(max_length=255, blank=True, null=True, default='...')
    status= models.BooleanField(default=True,null=True,blank=True)
    nb_views=models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title



class Contact(models.Model):
    name= models.CharField(max_length=60,null=False, blank=False, default='Anonymous')
    email= models.EmailField(max_length=255,null=False, blank=False)
    message=models.TextField(null=True, blank=True)
    date_sent=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
