from django.contrib import admin
from .models import post
# Register your models here.


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','content_size' ,'status','created_at', 'updated_at']
    actions = ['make_published', 'make_draft']
    def content_size(self,post):
        return '{}글자'.format(len(post.content))
    
    content_size.short_description = '내용글자수'

    def make_draft(self,request,queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request,'{}건의 포스팅을 draft상태로'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 draft 상태로 변경합니다'


    def make_published(self,request,queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request,'{}건의 포스팅을 published상태로'.format(updated_count))
    make_published.short_description = '지정 포스팅을 published 상태로 변경합니다'
#admin.site.register(post,PostAdmin)

 