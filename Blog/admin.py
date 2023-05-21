from django.contrib import admin

from .models import Tag,Blogauthor,Post

# Register your models here.

admin.site.register(Blogauthor)
admin.site.register(Post)

admin.site.register(Tag)

