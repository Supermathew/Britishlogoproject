from django.db import models



class MediaBucket(models.Model):
    image = models.ImageField(upload_to='media/')
    image_name = models.CharField(max_length=255)

    def __str__(self):
        return self.image_name

class VideoBucket(models.Model):
    video = models.FileField(upload_to='video/')
    video_name = models.CharField(max_length=255)

    def __str__(self):
        return self.video_name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubMenu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Footer(models.Model):
    Footerlogo = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True)
    discription = models.TextField(null=True,blank=True)
    britishlogo = models.TextField(null=True,blank=True)
    capabalities = models.TextField(null=True,blank=True)
    support = models.TextField(null=True,blank=True)
    copyright = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'Footer section'


class Social(models.Model):
    SocialImage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True)
    socialmedia = models.TextField(null=True,blank=True)
    url = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.socialmedia



class FooterSectionOne(models.Model):
    text = models.TextField(null=True,blank=True)
    url = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.text


class FooterSectionTwo(models.Model):
    text = models.TextField(null=True,blank=True)
    url = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.text


class FooterSectionThree(models.Model):
    text = models.TextField(null=True,blank=True)
    url = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.text



class Headerlogo(models.Model):
    headerlogo = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True)
    bookademo = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'logo'