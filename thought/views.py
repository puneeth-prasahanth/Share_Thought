from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from .models import *
from .forms import ReviewForms
import datetime
from django.http import HttpResponse
from django.views.generic.edit import FormView
#from .forms import TweetForm
#from django.views import View

# Create your views here.

import tweepy
consumer_key = 'VR95CmIMrv7q7vfDoPcjC8NZS'
consumer_secret = 'YlWo6BzDnhXozSZnvnN1cIcjvRKrJFJVnYA9vvqMDocOdjyBNu'
access_key = '1006840281361047553-JQPFugH9xVNifKRY1b4BjgpdTLiVND'
access_secret =   '5R3DXQmf6Xf3FwZHZzqSU3P3oYQAReUqwux9ttj5Gj7K5'

last_id=-1
flag=0

def index(request):
    topics=Topic.objects.all()
    context={
        'topics':topics,
    }
    return render(request,'base.html',context)


def thought(request,topic_id):

    topic=Topic.objects.get(pk=topic_id)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    dat=datetime.date.today()-datetime.timedelta(1)
    ##number_of_tweets=100
    date=str(dat)
    twitterData = {}
    i=1
    ##last_id=-1
    todate='0'
    #print(f'{int(date[8:10])} > {(int(todate)-1)}')
    #while (int(date[8:10]) > (int(todate)-1) ):
    while (i==1):
        #i=1
        global flag
        global last_id
        if flag > 0:
            tweets = api.search(q=topic,count=100,since=dat, lang="en", max_id=str(last_id - 1) )
        else:
            tweets = api.search(q=topic,count=100,since=dat, lang="en")
        for tweet in tweets:
            ##print(tweet.text)
            #print(request.user.id)
            if request.user.id is not None and Comment.objects.filter(user=request.user , tweet_id=tweet.id ).count()==1:
                comment=Comment.objects.get(user=request.user , tweet_id=tweet.id )
                tweet.comment=comment.text

            dummy_dict={i:tweet}
            twitterData.update(dummy_dict)
            todate=str(tweet.created_at)[8:10]
            i+=1

            last_id=tweet.id
        #searchedData = str(twitterData)
        # comment_details=Comment.objects.filter(user=request.user , tweet_id=id, ).values()
        #print(f'{todate}${last_id}')

    context={'twitterData':twitterData,'topic_id':topic_id}
    #if request.user.is_authenticated():
    return render(request,'base.html',context)
    #else:
         #return redirect ('index')

def comment(request,*args):
    """
    This Method holdes all the business logic of how comments are
    made and how we can store them and update them back to DB
    :param request:
    :param Id (int)  topic_id(int):
    :return: redirects to thought
    """
    id=args[0]
    topic_id=args[1]
    topic=Topic.objects.get(pk=topic_id)
    if request.method == "POST":
        form=ReviewForms(request.POST)
        if form.is_valid():
                #form=ReviewForms(request.POST)

            if Comment.objects.filter(user=request.user , tweet_id=id ).count()<1:
                x=form.cleaned_data.get('text')
                #print(f'{x}')
                new_comment=Comment.objects.create(
                    user=request.user,
                    text=form.cleaned_data.get('text'),
                    tweet_id=id
                    )
                new_comment.save()
            elif Comment.objects.filter(user=request.user , tweet_id=id ).count()==1:
                x=form.cleaned_data.get('text')
                Comment.objects.filter(user=request.user , tweet_id=id ).update(text=form.cleaned_data.get('text'))

            # this Flag Global variable used to control the twitter Api call
            flag=1
    return redirect ('thought', topic_id)




