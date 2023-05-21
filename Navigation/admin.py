from django.contrib import admin
from .models import MediaBucket,Menu,SubMenu,Footer,Social,FooterSectionOne,FooterSectionTwo,FooterSectionThree,VideoBucket,Headerlogo

# Register your models here.
admin.site.register(MediaBucket)
admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(Footer)
admin.site.register(Social)
admin.site.register(FooterSectionOne)
admin.site.register(FooterSectionTwo)
admin.site.register(FooterSectionThree)

admin.site.register(VideoBucket)

admin.site.register(Headerlogo)