from django.contrib import admin
from .models import *
# Register your models here.

class TESTSADMIN(admin.ModelAdmin):
    list_display = ('question','modul','answer0','answer1','answer2','answer3')
    search_fields = ('question','modul','answer0')
    list_filter = ('modul',)

class BOOKSADMIN(admin.ModelAdmin):
    list_display = ('name','discription','image','way')
    search_fields = ('name','discription')

class VIDEOSADMIN(admin.ModelAdmin):
    list_display = ('title','description')
    search_fields = ('title','description')

admin.site.register(TEST,TESTSADMIN)
admin.site.register(BOOKS,BOOKSADMIN)
admin.site.register(VIDEOS,VIDEOSADMIN)
# admin.site.register(TEST)
# admin.site.register(VIDEOS)