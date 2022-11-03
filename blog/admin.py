from django.contrib import admin

# Register your models here.
from . models import Post, A

admin.site.register(Post),
admin.site.register(A)