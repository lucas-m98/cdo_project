from __future__ import unicode_literals
from django.shortcuts import render
from . import forms
from reddit_api_call import call, StatusCodeError


# Create your views here.
def home(request):
    posts = {}
    context = {}
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            try:
                posts = call(request.POST['sub_reddit'])
                context['code'] = False
            except StatusCodeError as e:
                posts = False
                context['code'] = e.code
        else:
            posts = False
            context['code'] = "Internal: submitted form was invalid"
    else:
        form = forms.SearchForm()
    context['form'] = form
    context['posts'] = posts

    return render(request, "pull_reddit/home.html", context)