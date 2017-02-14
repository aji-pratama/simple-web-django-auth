from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from django.template import RequestContext
from django.contrib.auth.models import *
from django.contrib import auth

def home(request):
    return render_to_response('page.html', locals(), context_instance=RequestContext(request))

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
    return HttpResponse("Hahah")

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
