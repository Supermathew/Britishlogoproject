from django.db import models
from Navigation.models import MediaBucket
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.

class Blogauthor(models.Model):
    profilephoto = models.ForeignKey(MediaBucket, on_delete=models.CASCADE)
    bio = models.TextField()
    Position = models.TextField()
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Tag(models.Model):
    tag = models.TextField()

    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Post Title')
    category = models.CharField(max_length=50,null=True,blank=True)
    thumbnail = models.ForeignKey(MediaBucket, on_delete=models.CASCADE)
    Postauthor = models.ForeignKey(Blogauthor, on_delete=models.CASCADE)
    body = RichTextUploadingField(verbose_name='Compose Content')
    summary = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


