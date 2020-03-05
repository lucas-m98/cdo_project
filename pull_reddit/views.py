# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import response, request
from django.shortcuts import render
from . import forms
from reddit_api_call import call
from post import RedditPost

# Create your views here.
def home(request):
    posts = {}
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            # TODO:
            # - Check input to verify that you get back a subreddit properly
            # - Align images and make them size correctly
            #   - Make images not appear when there are none
            # - Make it pretty
            print("HERE")
            posts = call(request.POST['sub_reddit'])
        else:
            return response.HttpResponse("error")
    else:
        form = forms.SearchForm()
    context = {
        'form': form,
        'posts': posts
    }
    return render(request, "pull_reddit/home.html", context)
