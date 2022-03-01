from django.contrib import admin

# Register your models here.
from .models import *
class SocialLinkAdmin(admin.ModelAdmin):
    list_display=('phone','telegram','instagram','facebook','linkedin','youtube')
admin.site.register(SofialLinks,SocialLinkAdmin)
admin.site.register([Portfolio,Profile,Lessons,Resume,Visitors,Xabar])
