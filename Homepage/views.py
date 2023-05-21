from django.shortcuts import render
from .models import Review,Faq,Details,SliderImage,Homepage
from Navigation.models import Menu,SubMenu,Footer,Social,FooterSectionOne,FooterSectionTwo,FooterSectionThree,Headerlogo
from Blog.models import Post
# Create your views here.
def home(request):
    headerlogo = Headerlogo.objects.all().first()
    images = SliderImage.objects.all()
    review = Review.objects.all()
    faq = Faq.objects.all()
    details = Details.objects.all()
    homepage = Homepage.objects.all().first()
    footersectionone = FooterSectionOne.objects.all()
    footersectiontwo = FooterSectionTwo.objects.all()
    footersectionthree = FooterSectionThree.objects.all()
    social = Social.objects.all()
    footer = Footer.objects.all().first()
    menu = Menu.objects.all()
    blog = Post.objects.all()
    small_images = [image for image in images if image.size == 'small']
    large_images = [image for image in images if image.size == 'large']
    result =[]
    i = 0
    j = 0
    
    while i+1 < len(large_images) and j+1 < len(small_images):
          result.append(large_images[i])
          result.append(large_images[i+1])
          result.append(small_images[j])
          result.append(small_images[j+1])
        
          i += 2
          j += 2
    
    # Add any remaining big images if they exist
    result.extend(large_images[i:])
    
    # Add any remaining small images if they exist
    result.extend(small_images[j:])
    print(result)
    print(large_images)
    print(small_images)
    context = {
        'review': review,
        'faq': faq,
        'details': details,
        'homepage': homepage,
        'footersectionone': footersectionone,
        'footersectiontwo': footersectiontwo,
        'footersectionthree': footersectionthree,
        'social': social,
        'footer': footer,
        'menu': menu,
        'small_images': small_images,
        'large_images': large_images,
        'headerlogo': headerlogo,
        'result':result,
        'blog':blog
            }
    return render(request, 'home.html',context)