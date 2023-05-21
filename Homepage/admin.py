from django.contrib import admin

from .models import Review,Faq,Details,SliderImage,Homepage

# Register your models here.


admin.site.register(Review)
admin.site.register(Faq)

admin.site.register(Details)

admin.site.register(SliderImage)

admin.site.register(Homepage)


