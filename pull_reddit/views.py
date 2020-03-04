# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import response, request
from django.shortcuts import render
from . import forms
from reddit_api_call import call

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            # TODO:
            # - Get the search from the request
            # - Use the reddit API to search for the the input
            # - Parse the JSON to format it into a loop-able dictionary of posts
            #   that are then formatted into html
            call(request.POST['sub_reddit'])
            return response.HttpResponse(request.POST['sub_reddit'])
    else:
        form = forms.SearchForm()
    context = {
        'form': form
    }
    return render(request, "pull_reddit/home.html", context)
