from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from .models import About, Post

from django.template import RequestContext
from django.contrib.auth.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def index(request):
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            cek_auth = auth.authenticate(username=username, password=password)
            auth.login(request, cek_auth)
        except Exception, err:
            return HttpResponse('Login Gagal')
        else:
            return HttpResponseRedirect('/dashboard/')
    return render_to_response('login.html', locals(), context_instance=RequestContext(request))

@login_required
def dashboard(request):
    if request.user.is_authenticated():
        return render_to_response('dashboard.html', locals(), context_instance=RequestContext(request))
    return HttpResponse('Hanya bisa di askses oleh User')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        staff = False
        if request.POST.get('staff'):
            staff = True
        u = User.objects.create_user(username=username, password=password, email=email)
        u.first_name = first_name
        u.last_name = last_name
        u.is_staff = staff
        u.save()
        return HttpResponseRedirect('/')
    return render_to_response('register.html', locals(), context_instance=RequestContext(request))

def about(request):
    about = About.objects.get(id=1)
    return render_to_response('about.html', locals(), context_instance=RequestContext(request))

def about_detail(request):
    about = About.objects.get(id=1)
    return render_to_response('about_detail.html', locals(), context_instance=RequestContext(request))

def portfolio(request):
    return render_to_response('portfolio.html', locals(), context_instance=RequestContext(request))
