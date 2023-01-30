from email.mime import image
from xmlrpc.client import FastUnmarshaller
from django.db import models
from users.models import User

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField


# from cloudinary.models import CloudinaryField
# class myphotos(models.Model):
#     # title field
#     title = models.CharField(max_length=100)
#     #image field
#     image = CloudinaryField('image')
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True, null=True)
    details_description =  RichTextField( null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
# class GroupMember(models.Model)
