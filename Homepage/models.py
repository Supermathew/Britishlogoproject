from django.db import models

# Create your models here.

from Navigation.models import MediaBucket,VideoBucket


class Review(models.Model):
    userphoto = models.ForeignKey(MediaBucket, on_delete=models.CASCADE)
    text = models.TextField()
    video = models.ForeignKey(VideoBucket, on_delete=models.CASCADE,null=True,blank=True)
    watchvideo = models.TextField()

    def __str__(self):
        return self.text


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()


    def __str__(self):
        return self.question


class Details(models.Model):
    detailsphoto = models.ForeignKey(MediaBucket, on_delete=models.CASCADE)
    detailsquestion = models.TextField()
    detailsanswer = models.TextField()

    def __str__(self):
        return self.detailsquestion


class SliderImage(models.Model):
    SIZE_CHOICES = (
        ('small', 'Small'),
        ('large', 'Large'),
    )
    caption = models.TextField()
    sliderimage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)

    def __str__(self):
        return self.size


class Homepage(models.Model):
    text1 = models.TextField(null=True,blank=True)
    text2 = models.TextField(null=True,blank=True)
    Buttontext3 = models.TextField(null=True,blank=True)
    Buttontext4 = models.TextField(null=True,blank=True)
    text5 = models.TextField(null=True,blank=True)
    text6 = models.TextField(null=True,blank=True)                                                          
    text7 = models.TextField(null=True,blank=True)                                                       
    Buttontext8 = models.TextField(null=True,blank=True)                                                           
    Buttontext9 = models.TextField(null=True,blank=True)                                                            
    aboutimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='homepage_aboutimg')                                    
    aboutimgcan = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_aboutimgcan') 
    pencilimage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_pencilimage')              
    text10 = models.TextField(null=True,blank=True)                                                        
    text11 = models.TextField(null=True,blank=True)
    buttontext12 = models.TextField(null=True,blank=True)
    buttontext13 = models.TextField(null=True,blank=True)
    afoursizeimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_afoursizeimg')  
    crownimg1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_crownimg1')  
    crownimg2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_crownimg2')  
    crownimg3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_crownimg3')  
    crownimg4 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_crownimg4') 
    text14 = models.TextField(null=True,blank=True)
    text15 = models.TextField(null=True,blank=True)
    text16 = models.TextField(null=True,blank=True)
    text17 = models.TextField(null=True,blank=True)
    text18 = models.TextField(null=True,blank=True)
    text19 = models.TextField(null=True,blank=True)
    text20 = models.TextField(null=True,blank=True)
    text21 = models.TextField(null=True,blank=True)
    text22 = models.TextField(null=True,blank=True)
    text23 = models.TextField(null=True,blank=True)
    text24 = models.TextField(null=True,blank=True)
    text25 = models.TextField(null=True,blank=True)
    text26 = models.TextField(null=True,blank=True)
    google = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_google')  
    facebook = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_facebook')  
    hubspot3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_hubspot3')  
    googleads = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_googleads')  
    googlenetwork = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_googlenetwork')  
    youtubeads = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_youtubeads')
    text33 = models.TextField(null=True,blank=True)
    text34 = models.TextField(null=True,blank=True)
    text35 = models.TextField(null=True,blank=True)
    buttontext36 = models.TextField(null=True,blank=True)
    buttontext37 = models.TextField(null=True,blank=True)
    video1poster = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_video1poster')  
    video1 = models.ForeignKey(VideoBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_video1') 
    text27svg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_text27svg')  
    text28svg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_text28svg')  
    text29svg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_text29svg')  
 
    text27 = models.TextField(null=True,blank=True)
    text28 = models.TextField(null=True,blank=True)
    text29 = models.TextField(null=True,blank=True)
    text38 = models.TextField(null=True,blank=True)
    text39 = models.TextField(null=True,blank=True)
    buttontext40 = models.TextField(null=True,blank=True)
    buttontext41 = models.TextField(null=True,blank=True)
    soccer = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_soccer')  
    soccerblur = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_soccerblur')  
    text30 = models.TextField(null=True,blank=True)
    text31 = models.TextField(null=True,blank=True)
    video2 = models.ForeignKey(VideoBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_video2')  
    text32 = models.TextField(null=True,blank=True)
    ctavideoposter = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_ctavideoposter')  
    buttontext42 = models.TextField(null=True,blank=True)
    text43 = models.TextField(null=True,blank=True)
    text44 = models.TextField(null=True,blank=True)
    buttontext45 = models.TextField(null=True,blank=True)
    thumpsup = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_thumpsup')
    svg1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_svg1')
    svg2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_svg2')
    svg3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_svg3')
    text46 = models.TextField(null=True,blank=True)
    text47 = models.TextField(null=True,blank=True)
    text48 = models.TextField(null=True,blank=True)
    DailyBlogs = models.TextField(null=True,blank=True)
    buttontext42 = models.TextField(null=True,blank=True)
    cup = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True, related_name='homepage_cup')
    text49 = models.TextField(null=True,blank=True)
    text50 = models.TextField(null=True,blank=True)
    buttontext51 = models.TextField(null=True,blank=True)
    text52 = models.TextField(null=True,blank=True)
    text53 = models.TextField(null=True,blank=True)
    LearnMorebutton = models.TextField(null=True,blank=True)
     
    def __str__(self):
        return f'Homepage'




