from django.contrib import admin

from main.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('brand','title','price')

admin.site.register(Post, PostAdmin)