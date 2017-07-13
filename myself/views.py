from django.shortcuts import render, HttpResponseRedirect
from  django.http import HttpResponse
from myself.models import Post
from myself.forms import PostForm
import datetime

# Create your views here.

def index(request):
    my_dict= dict()
    my_dict["name"] = "Rodrigue le plus beau"
    my_dict["fruits"] = ["apple", "banana", "berries"]

    my_dict["all_posts"] = Post.objects.all()

    return render(request,'index.html', my_dict)

def new_post(request):
    if request.method == 'POST':
        filled_form =PostForm(request.POST)
        post = filled_form.save(commit=False)
        post.date=datetime.datetime.now()
        post.save()
        return HttpResponseRedirect('/myself')

    data=dict()
    new_post = PostForm()
    data["post_form"] = new_post
    return render(request, 'new_post.html', data)