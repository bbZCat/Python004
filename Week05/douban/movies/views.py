from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Avg

from .models import Comments

def index(request):
    moviename = '电话 콜 (2020)'
    movieurl = 'https://movie.douban.com/subject/30346025/'

    comms_all = Comments.objects.all()    
    filter = {'star__gt':3}
    comms = comms_all.filter(**filter)
    return render(request, 'index.html', locals())
