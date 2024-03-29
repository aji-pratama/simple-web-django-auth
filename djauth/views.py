from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import About, Komentar, Gambar
from django.utils import timezone

from django.template import RequestContext
from django.contrib.auth.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test

# JUST FOR ADMIN
@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    if request.user.is_authenticated():
        return render_to_response('admin/dashboard.html', locals(), context_instance=RequestContext(request))
    return HttpResponse('Hanya bisa di askses oleh User')

@user_passes_test(lambda u: u.is_superuser)
def about_edit(request):
    about = About.objects.get(id=1)
    if request.POST:
        about.title = request.POST.get('title')
        about.desc = request.POST.get('desc')
        about.desc_detail = request.POST.get('desc_detail')
        about.tgl_post = timezone.now()
        about.save()
        return render_to_response('admin/about.html', locals(), context_instance=RequestContext(request))
    return render_to_response('admin/edit_about.html', locals(), context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
def about_create(request):
    if request.POST:
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        desc_detail = request.POST.get('desc_detail')
        tgl_post = timezone.now()
        about = About(title=title,desc=desc,desc_detail=desc_detail,tgl_post=tgl_post)
        about.save()
        return render_to_response('admin/about.html', locals(), context_instance=RequestContext(request))
    return render_to_response('admin/about.html', locals(), context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
def upload_gambar(request):
    gambar = Gambar.objects.all().order_by('-id')
    if request.POST:
        nama = request.POST.get('nama')
        gambars = request.FILES.get('gambar')
        ga = Gambar(nama=nama, gambar=gambars)
        ga.save()
        image_result = open('media/image_upload/%s' % gambars,'wb')
        image_result.write(gambars.read())

        gambar = Gambar.objects.all()
        return render_to_response('admin/upload_gambar.html', locals(), context_instance=RequestContext(request))
    return render_to_response('admin/upload_gambar.html', locals(), context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
def about_admin(request):
    try:
        about = About.objects.get(id=1)
        return render_to_response('admin/about.html', locals(), context_instance=RequestContext(request))
    except Exception, err:
        about = False
        return render_to_response('admin/about.html', locals(), context_instance=RequestContext(request))

# FOR MEMBER LOGGED IN NON ADMIN & ADMIN
@user_passes_test(lambda u: u.is_active)
def about_komentar(request):
    about = About.objects.get(id=1)
    komentar = Komentar.objects.filter(untuk='about')
    if request.user.is_authenticated():
        if request.POST:
            body = request.POST.get('body')
            komentator = request.POST.get('komentator')
            untuk = request.POST.get('untuk')

            k = Komentar(body=body, komentator=komentator, untuk=untuk)
            k.save()

            return render_to_response('about_detail.html', locals(), context_instance=RequestContext(request))
    return HttpResponse('Hanya bisa di askses oleh User')

@user_passes_test(lambda u: u.is_active)
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

# FOR EVERYONE
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
            if User.objects.filter(is_superuser=1):
                return HttpResponseRedirect('/dashboard/')
            else:
                return HttpResponseRedirect('/')
    return render_to_response('login.html', locals(), context_instance=RequestContext(request))

def index(request):
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

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
    try:
        about = About.objects.get(id=1)
        return render_to_response('about.html', locals(), context_instance=RequestContext(request))
    except Exception, err:
        about = False
        return render_to_response('about.html', locals(), context_instance=RequestContext(request))

def about_detail(request):
    about = About.objects.get(id=1)
    komentar = Komentar.objects.filter(untuk='about')
    return render_to_response('about_detail.html', locals(), context_instance=RequestContext(request))

def portfolio(request):
    gambar = Gambar.objects.all()
    # komentator = Komentar.objects.filter(untuk='komentar')
    return render_to_response('portfolio.html', locals(), context_instance=RequestContext(request))



#
