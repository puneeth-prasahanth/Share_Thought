from django.contrib import admin

from .models import Comment,Topic


class TopicModels(admin.ModelAdmin):


    list_display = ('topic',)


class CommentModels(admin.ModelAdmin):


    list_display = ('user','Publish_date','text','tweet_id')




#class AuthorModels(admin.ModelAdmin):
#    list_display = ('first_name','middle_name','last_name')

admin.site.register(Comment,CommentModels)
admin.site.register(Topic,TopicModels)
