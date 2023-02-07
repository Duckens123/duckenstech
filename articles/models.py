from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    #category= models.ForeignKey(Category,related_name="category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    content = models.TextField(blank=True, null=True)
    datepublished= models.DateTimeField(auto_now_add=True)
    lastupdated= models.DateTimeField(auto_now=True)
    publishedby= models.ForeignKey(User,  on_delete=models.CASCADE)
    imagethumbnail= models.ImageField(upload_to="articles/static/articles/images/post")
    imagecaptions= models.CharField(max_length=255, blank=True, null=True, default='...')
    status= models.BooleanField(default=True,null=True,blank=True)
    nb_views=models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title
